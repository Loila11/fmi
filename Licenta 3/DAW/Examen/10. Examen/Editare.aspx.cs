using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Globalization;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Editare : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // Afisare formular de editare
        if (!Page.IsPostBack && Request.Params["id"] != null)
        {
            // Luam ID-ul
            int ID = int.Parse(Request.Params["id"].ToString());
            // Salvam cererea SQL intr-un string
            string query = "SELECT * "
                    + " FROM angajat join departament on angajat.id = departament.id_angajat join salarii on angajat.id = salarii.id_angajat "
                    + " WHERE angajat.id = @id";

            // Deschidem conexiunea la baza de date
            SqlConnection con = new SqlConnection(@"Data Source=.\SQLEXPRESS;AttachDbFilename='C:\Facultate Materiale\Materii Predate\Dezvoltarea Aplicatiilor Web\Laboratoare\10. ModelExamen\App_Data\BazaDeDate.mdf';Integrated Security=True;User Instance=True");
            con.Open();
           
            try
            {
                // Se construieste comanda SQL
                SqlCommand com = new SqlCommand(query, con);
                com.Parameters.AddWithValue("id", ID);

                // Se executa comanda si se returneaza valorile intr-un reader
                SqlDataReader reader = com.ExecuteReader();

                // Citim rand cu rand din baza de date
                while (reader.Read())
                {
                    Nume.Text = reader["nume"].ToString();
                    Prenume.Text = reader["prenume"].ToString();
                    DataNasterii.Text = DateTime.Parse(reader["data_nasterii"].ToString()).ToShortDateString();
                    DataAngajarii.Text = DateTime.Parse(reader["data_angajare"].ToString()).ToShortDateString();
                    DenDepart.Text = reader["denumire"].ToString();
                    DeLaDataDepart.Text = DateTime.Parse(reader["de_la_data"].ToString()).ToShortDateString();
                    PanaLaDataDepart.Text = DateTime.Parse(reader["pana_la_data"].ToString()).ToShortDateString();
                    DeLaDataSal.Text = DateTime.Parse(reader["de_la_data"].ToString()).ToShortDateString();
                    PanaLaDataSal.Text = DateTime.Parse(reader["pana_la_data"].ToString()).ToShortDateString();
                    ValSal.Text = reader["valoare_salariu"].ToString();

                }
            }
            catch (Exception ex)
            {
                EroareBazaDate.Text = "Eroare din baza de date: " + ex.Message;
            }
            finally
            {
                con.Close();
            }
        }
    }

    protected void editare(object sender, EventArgs e)
    {
        if (Page.IsValid && Request.Params["id"] != null)
        {
            int ID = int.Parse(Request.Params["id"].ToString());
            
            string _Nume = Nume.Text;
            string _Prenume = Prenume.Text;
            DateTime _DataNasterii = DateTime.Parse(DataNasterii.Text);
            DateTime _DataAngajarii = DateTime.Parse(DataAngajarii.Text);
            string _DenDepart = DenDepart.Text;
            DateTime _DeLaDataDepart = DateTime.Parse(DeLaDataDepart.Text);
            DateTime _PanaLaDataDepart = DateTime.Parse(PanaLaDataDepart.Text);
            DateTime _DeLaDataSal = DateTime.Parse(DeLaDataSal.Text);
            DateTime _PanaLaDataSal = DateTime.Parse(PanaLaDataSal.Text);
            string _ValSal = ValSal.Text;


            string query = "UPDATE angajat "
                  + "SET nume = @nume, prenume = @prenume, data_nasterii = @data_nasterii, data_angajare = @data_angajare "
                  + "  WHERE id = @id ";

            SqlConnection con = new SqlConnection(@"Data Source=.\SQLEXPRESS;AttachDbFilename='C:\Facultate Materiale\Materii Predate\Dezvoltarea Aplicatiilor Web\Laboratoare\10. ModelExamen\App_Data\BazaDeDate.mdf';Integrated Security=True;User Instance=True");

            con.Open();

            try
            {
                // Introducem parametrii in cererea SQL
                SqlCommand com = new SqlCommand(query, con);
                
                com.Parameters.AddWithValue("id", ID);
                com.Parameters.AddWithValue("nume", _Nume);
                com.Parameters.AddWithValue("prenume", _Prenume);
                com.Parameters.AddWithValue("data_nasterii", _DataNasterii);
                com.Parameters.AddWithValue("data_angajare", _DataAngajarii);


                com.ExecuteNonQuery(); 
                

                // inserare noua
                string query2 = "UPDATE departament "
               + "SET denumire = @denumire, de_la_data = @de_la_data, pana_la_data = @pana_la_data "
               + "WHERE id_angajat = @id;";
              
                SqlCommand com2 = new SqlCommand(query2, con);

                com2.Parameters.AddWithValue("id", ID);
                com2.Parameters.AddWithValue("denumire", _DenDepart);
                com2.Parameters.AddWithValue("de_la_data", _DeLaDataDepart);
                com2.Parameters.AddWithValue("pana_la_data", _PanaLaDataDepart);

                com2.ExecuteNonQuery();
                

                string query3 = "UPDATE salarii "
               + "SET de_la_data = @de_la_data, pana_la_data = @pana_la_data, valoare_salariu = @valoare_salariu "
               + "WHERE id_angajat = @id;"; 

                SqlCommand com3 = new SqlCommand(query3, con);

                com3.Parameters.AddWithValue("id", ID);
                com3.Parameters.AddWithValue("de_la_data", _DeLaDataSal);
                com3.Parameters.AddWithValue("pana_la_data",_PanaLaDataSal);
                com3.Parameters.AddWithValue("valoare_salariu", _ValSal);

                 com3.ExecuteNonQuery(); 
            }
            catch (Exception ex)
            {
                EroareBazaDate.Text = "Eroare din baza de date: " + ex.Message;
            }
            finally
            {

                con.Close();
            }
            


        }
    }
}