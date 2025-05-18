import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Diyagram boyutu
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.axis('off')

def draw_class(x, y, title, attributes, methods, width=4, height=3):
    ax.add_patch(patches.Rectangle((x, y - height), width, height, fill=True, edgecolor='black', facecolor='white'))
    ax.text(x + width/2, y - 0.5, title, ha='center', va='top', fontsize=10, weight='bold')
    attr_text = "\n".join(attributes)
    method_text = "\n".join(methods)
    ax.text(x + 0.1, y - 1.2, attr_text, va='top', fontsize=8, family='monospace')
    ax.text(x + 0.1, y - 2.3, method_text, va='top', fontsize=8, family='monospace')

def draw_arrow(x1, y1, x2, y2, style='->', label=None):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, lw=1))
    if label:
        ax.text((x1 + x2)/2, (y1 + y2)/2, label, fontsize=8, ha='center', va='center')

# Sınıflar
draw_class(2, 18, 'User', ['- id: int', '- name: str', '- email: str', '- role: enum'], ['+ login()', '+ logout()'])
draw_class(1, 13, 'Candidate', ['- cv: CVFile', '- profile: Profile'], ['+ uploadCV()', '+ viewFeedback()'])
draw_class(5, 13, 'Employer', ['- jobPostings: list', '- criteria: list'], ['+ createJob()', '+ setCriteria()'])
draw_class(0, 8, 'CVFile', ['- content: str', '- format: enum'], [])
draw_class(6, 8, 'JobPosting', ['- title: str', '- desc: str'], [])
draw_class(12, 8, 'Criteria', ['- name: str', '- weight: float'], [])
draw_class(10, 13, 'EvaluationEngine', [], ['+ analyzeCV()', '+ scoreCandidate()', '+ generateReport()'])
draw_class(10, 4, 'EvaluationReport', ['- content: str'], ['+ export()'])

# İlişkiler
draw_arrow(3, 15, 3, 13.2, '-|>', label='inherits')  # Candidate -> User
draw_arrow(6, 15, 6, 13.2, '-|>', label='inherits')  # Employer -> User
draw_arrow(2, 12.5, 1.5, 10.8)                       # Candidate -> CVFile
draw_arrow(5.5, 12.5, 6.5, 10.8)                     # Employer -> JobPosting
draw_arrow(7.8, 8.5, 11.8, 8.5, style='-|>', label='composed')  # JobPosting -> Criteria
draw_arrow(10.5, 12.8, 1.5, 9.2, style='dashed')     # Eval -> CVFile
draw_arrow(10.5, 12.8, 6.5, 9.2, style='dashed')     # Eval -> JobPosting
draw_arrow(10.5, 12.8, 11.8, 9.2, style='dashed')    # Eval -> Criteria
draw_arrow(10.5, 12.5, 10.5, 5.5)                    # Eval -> Report

plt.tight_layout()
plt.savefig("/mnt/data/resume_ranker_class_diagram.png", dpi=300)
plt.show()
