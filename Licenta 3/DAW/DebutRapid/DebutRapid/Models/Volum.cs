using System;
using System.Data.Entity;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace DebutRapid.Models
{
    public class Volum
    {
        [Key]
        [Required]
        public int id { get; set; }
        [Required]
        public string denumire { get; set; }
    }
    public class DbCtx : DbContext
    {
        public DbCtx() : base("db2")
        {
            Database.SetInitializer<DbCtx>(new Initp());
        }
        public DbSet<Volum> Volume { get; set; }
        public DbSet<Poezie> Poezie { get; set; }
    }
    public class Initp : DropCreateDatabaseIfModelChanges<DbCtx>
    {
        public ICollection<Volum> Volume { get; private set; }

        protected override void Seed(DbCtx ctx)
        {
            Volum volum1 = new Volum { id = 1, denumire = "Ariel" };
            Volum volum2 = new Volum { id = 1, denumire = "Floare Albastra" };
            Volum volum3 = new Volum { id = 1, denumire = "Volum 3" };
            ctx.Volume.Add(volum1);
            ctx.Volume.Add(volum2);
            ctx.Volume.Add(volum3);

            ctx.Poezie.Add(new Poezie { id = 1, titlu = "Medusa", autor = "Sylvia Plath", numar_strofe = 3, volumId = 1, volum = Volume });
            ctx.Poezie.Add(new Poezie { id = 2, titlu = "Ariel", autor = "Sylvia Plath", numar_strofe = 4, volumId = 1, volum = Volume });
            ctx.Poezie.Add(new Poezie { id = 3, titlu = "Tullips", autor = "Sylvia Plath", numar_strofe = 6, volumId = 1, volum = Volume });
            ctx.Poezie.Add(new Poezie { id = 4, titlu = "Floare Albastra", autor = "Mihai Eminescu", numar_strofe = 4, volumId = 2, volum = Volume });
            ctx.Poezie.Add(new Poezie { id = 5, titlu = "Titlu 1", autor = "Autor 1", numar_strofe = 3, volumId = 3, volum = Volume });
            ctx.Poezie.Add(new Poezie { id = 6, titlu = "Titlu 2", autor = "Autor 2", numar_strofe = 2, volumId = 3, volum = Volume });
            ctx.SaveChanges();
            base.Seed(ctx);
        }
    }
}
