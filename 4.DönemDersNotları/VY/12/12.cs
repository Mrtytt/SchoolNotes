/*
    B ağacı

        Kapasite
            Her düğüm m/2 ya da m arasında anahtar içerir.
            Her düğüm m + 1 çocuğu vardır.
            Tüm yapraklar aynı seviyededir.
            Verileryapraklarda tutulur.
            Yaprak olmayan düğümler k çocuk ve k + 1 düğüm içerir.

    B+ ağacı
        d ağacın kapasitesidir. Root hariç
        m <= d <= 2m

        yüksekliği h = log_k(N)
        k = düğüm sayısı, N = kayıt sayısı

        Genelde %66 doluluk sağlar.

        Kapasite
            Her düğüm m/2 ya da m arasında anahtar içerir.
            Her düğüm m + 1 çocuğu vardır.
            Tüm yapraklar aynı seviyededir.
            Verileryapraklarda tutulur.
            Yaprak olmayan düğümler k çocuk ve k + 1 düğüm içerir.

        Indeks kısmını rame bilgiyi diske koyarak daha hızlı erişim sağlayabilir.
        Hem yapraklar algoritmik olarak hem de yapraklarda sıralı şekilde ulaşım şansımız var.

        Çocuk sayısı d + 1 < m < 2d + 1
        m = Çocuk sayısı
        Kök düğüm 1 <= m <= 2d düğüm tutabilir.

        Veriler sadece yaprakta olabilir. O yüzden yaparağa kadar inmek gerekir.
        
*/

public class BDugum
{
    int[] K;    // Keys 
    int m;      // Cocuk sayısı
    int d;      // Derece
    boolen yaprak;  //IsLeaf
    BDugum[] nesil;
    public BDugum(int d)
    {
        m = 0;
        this.d = d;
        yaprak = true;
        // Bu ağacın 1 fazla olmasının sebebi eklerken buraya gelecek.
        K = new int[2*d+1];
        nesil = new BDugum[2*d+1];
    }
}
public class BAgac
{

}
public BDugum agacAra(int eleman)
{

}

// Eklerken kapasiteyi aşarsak split ederiz ortanca değer yukarı çıkar.