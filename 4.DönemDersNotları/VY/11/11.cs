public class AvlDugum{
    int icerik;
    int boy;
    AvlDugum sol;
    AvlDugum sag;

    public AvlDugum(int icerik)
    {
        this.icerik = icerik;

    }
}
public class AvlAgaci{
    AvlDugum kok;
    public AvlAgaci(){
        kok = null;
    }
}
int boy(AvlDugum d){
    if (d == null)
        return 0;    
    else
        return d.boy;
}
