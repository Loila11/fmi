<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Afisare.aspx.cs" Inherits="Afisare" MasterPageFile="MasterPage.master" %>

<asp:Content runat="server" ContentPlaceHolderID="ContentPlaceHolder1">

    <form id="form1" runat="server">

        <h3> Afisare dupa valoare </h3>
        <br />
        <br />
    
        Introduceti valoare: 
        <asp:TextBox ID="ValoareSalariu" runat="server"></asp:TextBox>

        <asp:CompareValidator ID="CompareValidator1" runat="server" ControlToValidate="ValoareSalariu" ErrorMessage="Trebuie introdusa o valoare intreaga" Operator="DataTypeCheck" Type="Integer"></asp:CompareValidator>
        <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ErrorMessage="Campul este obligatoriu" ControlToValidate="ValoareSalariu"></asp:RequiredFieldValidator>

        <br />
        <asp:Button ID="Button1" runat="server" Text="Cauta" OnClick="search" />
        <br />
        <br />
        <asp:Literal ID="Status" runat="server"></asp:Literal>   
        <br />
        <br />

        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString='Data Source=.\SQLEXPRESS;AttachDbFilename="C:\Facultate Materiale\Materii Predate\Dezvoltarea Aplicatiilor Web\Laboratoare\10. ModelExamen\App_Data\BazaDeDate.mdf";Integrated Security=True;User Instance=True' SelectCommand="select * from [angajat] join [salarii] on (angajat.id = salarii.id_angajat) where salarii.valoare_salariu > @ValoareSalariu">
            <SelectParameters>
                <asp:Parameter Name="ValoareSalariu"  DefaultValue="0"/>
            </SelectParameters>
        </asp:SqlDataSource>
        <hr />

        <asp:ListView ID="ListView1" runat="server" DataSourceID="SqlDataSource1">
            <LayoutTemplate>
                <table runat="server" id="table1" >
                    <tr runat="server" id="itemPlaceholder" ></tr>
                </table>
            </LayoutTemplate>
            <ItemTemplate>
                <tr id="Tr1" runat="server">
                    <td style="color: #ac00dc"><%#Eval("nume") %></td>
                    <td><%#Eval("prenume") %></td>
                    <td style="color: #09c"><%#Eval("data_nasterii") %></td>
                    <td style="color: #ccc"><%#Eval("data_angajare") %></td>
                    <td style="color: #ccc"><%#Eval("valoare_salariu") %></td>
                </tr>
                <td>
                    <a href="Editare.aspx?id=<%#Eval("id") %>">Editare</a>
                    <!--<a href="Show.aspx?id=<%#Eval("id") %>">Vizualiare</a> |
                    <a href="Delete.aspx?id=<%#Eval("id") %>">Stergere</a>-->
                    </td>
            </ItemTemplate>
        </asp:ListView>

    </form>
</asp:Content>
