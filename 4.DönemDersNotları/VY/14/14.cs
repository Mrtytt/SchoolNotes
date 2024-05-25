using System;

namespace App
{
    public class Oge
    {
        public int icerik,ebeveyn, derinlik;
        public Oge(int icerik)
        {
            this.icerik = icerik;
            ebeveyn = icerik;
            derinlik = 1;
        }
    }
    public class Set
    {
        Oge[] kumeler;
        int kactane;

        public Set(int N)
        {
            kumeler = new Oge[N]
            kactane = N;
            for (int i = 0; i < N; i++)
                kumeler[i] = new Oge(i);
        }
        // Derinliği az olan çok olana eklenir aynıysa fark etmez.
        public int Find(int sira)
        {
            if (kumeler[sira].ebeveyn != sira)
                return Find(kumeler[sira].ebeveyn);
            return kumeler[sira].ebeveyn;
        }
        public void Union(int sira1,int sira2)
        {
            int x,y;
            x = Find(sira1);
            y = Find(sira2);

            if (kumeler[x].derinlik < kumeler[y].derinlik)
                kumeler[x].ebeveyn = y;
            else
            {
                kumeler[y].ebeveyn = x;
                if (kumeler[x].derinlik == kumeler[y].derinlik)
                    kumeler[x].derinlik++;
            }
        }
    }
}