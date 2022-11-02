using DebutRapid.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace DebutRapid.Controllers
{
    public class VolumController : Controller
    {
        private DbCtx db = new DbCtx();
        public ActionResult Index()
        {
            List<Volum> volum = db.Volume.ToList();
            ViewBag.Volume = volum;
            return View();
        }
    }
}
