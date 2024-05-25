public class eleman
{
    int içerik;
    int ad;
    public eleman(int oncelik,int ad)
    {
        this.oncelik = oncelik;
        this.ad = ad;
    }
}
public class maxHeap
{
    public eleman[] dizi;
    public int boyut;
    public int sayac;
    public maxHeap(int boyut)
    {
        dizi = new eleman[boyut];
        this.sayac = 0;
    }
    public int findMax()
    {
        return dizi[0].ad;
    }
    
}