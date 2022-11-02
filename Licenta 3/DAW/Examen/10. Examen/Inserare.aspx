<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Inserare.aspx.cs" Inherits="Inserare" MasterPageFile="MasterPage.master" %>

<asp:Content runat="server" ContentPlaceHolderID="ContentPlaceHolder1">

    <form id="form1" runat="server">
        <h3> Inserare angajat </h3>
        <br />
        <br />

         <table>
         <tr>
            <td>Nume: &nbsp;</td>
            <td><asp:TextBox ID="Nume" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="Nume" ErrorMessage="Numele este obligatoriu"></asp:RequiredFieldValidator>
            </td>
         </tr>

        <tr>
            <td>Prenume &nbsp;</td>
            <td><asp:TextBox ID="Prenume" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControlToValidate="Prenume" ErrorMessage="Prenumele este obligatoriu"></asp:RequiredFieldValidator>
            </td>
        </tr>

        <tr>
            <td>Data Nasterii: &nbsp;</td>
            <td><asp:TextBox ID="DataNasterii" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ControlToValidate="DataNasterii" ErrorMessage="Data nasterii este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator2" runat="server" ControlToValidate="DataNasterii" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>Data Angajarii: &nbsp;</td>
            <td><asp:TextBox ID="DataAngajarii" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator4" runat="server" ControlToValidate="DataAngajarii" ErrorMessage="Data ang este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator1" runat="server" ControlToValidate="DataAngajarii" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>Denumire Departament: &nbsp;</td>
            <td><asp:TextBox ID="DenDepart" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator5" runat="server" ControlToValidate="DenDepart" ErrorMessage="Denumire dept este obligatorie"></asp:RequiredFieldValidator>
            </td>
        </tr>
        
        <tr>
            <td>De la data (departament): &nbsp;</td>
            <td><asp:TextBox ID="DeLaDataDepart" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator6" runat="server" ControlToValidate="DeLaDataDepart" ErrorMessage="Data dept este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator4" runat="server" ControlToValidate="DeLaDataDepart" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>Pana la data (departament): &nbsp;</td>
            <td><asp:TextBox ID="PanaLaDataDepart" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator7" runat="server" ControlToValidate="PanaLaDataDepart" ErrorMessage="Data dept este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator3" runat="server" ControlToValidate="PanaLaDataDepart" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>
        
        <tr>
            <td>De la data (salariul): &nbsp;</td>
            <td><asp:TextBox ID="DeLaDataSal" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator8" runat="server" ControlToValidate="DeLaDataSal" ErrorMessage="Data dept este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator5" runat="server" ControlToValidate="DeLaDataSal" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>Pana la data (salariul): &nbsp;</td>
            <td><asp:TextBox ID="PanaLaDataSal" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator9" runat="server" ControlToValidate="PanaLaDataSal" ErrorMessage="Data dept este obligatorie"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator6" runat="server" ControlToValidate="PanaLaDataSal" ErrorMessage="Tip Data !" Operator="DataTypeCheck" Type="Date"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>Valoare salariu: &nbsp;</td>
            <td><asp:TextBox ID="ValSal" runat="server"></asp:TextBox></td>
            <td>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator10" runat="server" ControlToValidate="ValSal" ErrorMessage="Salariul este obligatoriu"></asp:RequiredFieldValidator>
                <asp:CompareValidator ID="CompareValidator7" runat="server" ControlToValidate="ValSal" ErrorMessage="Tip Int !" Operator="DataTypeCheck" Type="Integer"></asp:CompareValidator>
            </td>
        </tr>

        <tr>
            <td>
                <asp:Button ID="Button1" runat="server" OnClick="inserare" Text="Inserare" />
            </td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>

        <tr>
            <td><asp:Literal ID="EroareBazaDate" runat="server"></asp:Literal></td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </table>
  </form>
</asp:Content>