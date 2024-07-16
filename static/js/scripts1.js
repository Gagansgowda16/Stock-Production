function generatePDF(){
const element = document.getElementById("stockdetails");

html2pdf()
.form(element)
.save();

}