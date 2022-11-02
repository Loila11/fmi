using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Inserare : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void inserare(object sender, EventArgs e)
    {
        if (Page.IsValid)
        {
            string _Nume = Nume.Text;
            string _Prenume = Prenume.Text;
            string _DataNasterii = DataNasterii.Text;
            string _DataAngajarii = DataAngajarii.Text;
            string _DenDepart = DenDepart.Text;
            string _DeLaDataDepart = DeLaDataDepart.Text;
            string _PanaLaDataDepart = PanaLaDataDepart.Text;
            string _DeLaDataSal = DeLaDataSal.Text;
            string _PanaLaDataSal = PanaLaDataSal.Text;
            string _ValSal = ValSal.Text;

            string query = "INSERT INTO angajat"
                   + "(nume, prenume, data_nasterii, data_angajare) VALUES (@nume, @prenume, @data_nasterii, @data_angajare);"
                   + "SELECT CAST(scope_identity() AS int)";

            SqlConnection con = new SqlConnection(@"Data Source=.\SQLEXPRESS;AttachDbFilename='C:\Facultate Materiale\Materii Predate\Dezvoltarea Aplicatiilor Web\Laboratoare\10. ModelExamen\App_Data\BazaDeDate.mdf';Integrated Security=True;User Instance=True");
            con.Open();

            try
            {
                 // Introducem parametrii in cererea SQL
                    SqlCommand com = new SqlCommand(query, con);
                    com.Parameters.AddWithValue("nume", _Nume);
                    com.Parameters.AddWithValue("prenume", _Prenume);
                    com.Parameters.AddWithValue("data_nasterii", _DataNasterii);
                    com.Parameters.AddWithValue("data_angajare", _DataAngajarii);

                    
                    int id_inserare = (int) com.ExecuteScalar(); // Returneaza id-ul ultimei inserari
                    
                    // inserare noua
                    string query2 = "INSERT INTO departament"
                   + "(id_angajat, denumire, de_la_data, pana_la_data) VALUES (@id_angajat, @denumire, @de_la_data, @pana_la_data);"
                           + "SELECT CAST(scope_identity() AS int)";
                    SqlCommand com2 = new SqlCommand(query2, con);

                    com2.Parameters.AddWithValue("id_angajat", id_inserare);
                    com2.Parameters.AddWithValue("denumire", _DenDepart);
                    com2.Parameters.AddWithValue("de_la_data", _DeLaDataDepart);
                    com2.Parameters.AddWithValue("pana_la_data", _PanaLaDataDepart);

                    com2.ExecuteScalar(); // Returneaza id-ul ultimei inserari


                    string query3 = "INSERT INTO salarii"
                   + "(id_angajat, de_la_data, pana_la_data, valoare_salariu) VALUES (@id_angajat, @de_la_data, @pana_la_data, @valoare_salariu);"
                           + "SELECT CAST(scope_identity() AS int)";

                    SqlCommand com3 = new SqlCommand(query3, con);

                    com3.Parameters.AddWithValue("id_angajat", id_inserare);
                    com3.Parameters.AddWithValue("de_la_data", _DeLaDataSal);
                    com3.Parameters.AddWithValue("pana_la_data", _PanaLaDataSal);
                    com3.Parameters.AddWithValue("valoare_salariu", _ValSal);

                    com3.ExecuteScalar(); // Returneaza id-ul ultimei inserari
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