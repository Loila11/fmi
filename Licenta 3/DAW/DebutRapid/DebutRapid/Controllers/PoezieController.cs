// PoezieController.cs

using DebutRapid.Models;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;

namespace DebutRapid.Controllers
{
    public class PoezieController : Controller
    {
        private DbCtx db = new DbCtx();

        // GET: Poezie
        public ActionResult Index(string searchString)
        {
            var poezii = from m in db.Poezie select m;

            if (!String.IsNullOrEmpty(searchString))
            {
                poezii = poezii.Where(s => s.titlu.Contains(searchString));
            }
            foreach (var x in poezii.ToList())
            {
                Console.WriteLine(x.titlu);
            }

            return View(poezii.ToList());
        }

        // GET: Poezie/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Poezie poezie = db.Poezie.Find(id);
            if (poezie == null)
            {
                return HttpNotFound();
            }
            return View(poezie);
        }

        // GET: Poezie/Create
        public ActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "id,titlu,autor,numar_strofe,volum")] Poezie poezie)
        {
            if (ModelState.IsValid)
            {
                db.Poezie.Add(poezie);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(poezie);
        }

        // GET: Poezie/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Poezie poezie = db.Poezie.Find(id);
            if (poezie == null)
            {
                return HttpNotFound();
            }
            return View(poezie);
        }

        // POST: Poezie/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "id,titlu,autor,numar_strofe,volum")] Poezie poezie)
        {
            if (ModelState.IsValid)
            {
                db.Entry(poezie).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(poezie);
        }

        // GET: Poezie/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Poezie poezie = db.Poezie.Find(id);
            if (poezie == null)
            {
                return HttpNotFound();
            }
            return View(poezie);
        }

        // POST: Poezie/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Poezie poezie = db.Poezie.Find(id);
            db.Poezie.Remove(poezie);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
