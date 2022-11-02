using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace DebutRapid.Models
{
    public class Poezie
    {
        [Key]
        [Required]
        public int id { get; set; }
        [Required]
        public string titlu { get; set; }
        [Required]
        public string autor { get; set; }
        [Required]
        public int numar_strofe { get; set; }
        [ForeignKey("volumId")]
        public int volumId { get; set; }
        [Required]
        public ICollection<Volum> volum { get; set; }
    }
}
