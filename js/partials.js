// Navbar e footer condivisi, iniettati via JS in ogni pagina.
// Nessun fetch: funziona anche aprendo i file HTML direttamente dal filesystem.
// Ogni pagina imposta <body data-base-path="..."> con "" in root e "../" dentro frazioni/.
(function () {
  var FRAZIONI = [
    { slug: "civitella", nome: "Civitella (capoluogo)" },
    { slug: "albergo", nome: "Albergo" },
    { slug: "badia-al-pino", nome: "Badia al Pino" },
    { slug: "ciggiano", nome: "Ciggiano" },
    { slug: "cornia", nome: "Cornia" },
    { slug: "matroia", nome: "Matroia" },
    { slug: "oliveto", nome: "Oliveto" },
    { slug: "pieve-a-maiano", nome: "Pieve a Maiano" },
    { slug: "pieve-al-toppo", nome: "Pieve al Toppo" },
    { slug: "ponticino", nome: "Ponticino" },
    { slug: "spoiano", nome: "Spoiano" },
    { slug: "tegoleto", nome: "Tegoleto" },
    { slug: "tuori", nome: "Tuori" },
    { slug: "viciomaggio", nome: "Viciomaggio" }
  ];

  function renderNavbar(basePath) {
    var dropdownItems = FRAZIONI.map(function (f) {
      return '<a class="dropdown-item" href="' + basePath + "frazioni/" + f.slug + '.html">' + f.nome + "</a>";
    }).join("\n");

    return (
      '<nav class="navbar navbar-expand-lg navbar-dark bg-dark">' +
      '<div class="container px-lg-5">' +
      '<a class="navbar-brand" href="' + basePath + 'index.html">Civitella in Pillole</a>' +
      '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>' +
      '<div class="collapse navbar-collapse" id="navbarSupportedContent">' +
      '<ul class="navbar-nav ms-auto mb-2 mb-lg-0">' +
      '<li class="nav-item"><a class="nav-link" href="' + basePath + 'index.html">Home</a></li>' +
      '<li class="nav-item"><a class="nav-link" href="' + basePath + 'storia.html">Storia</a></li>' +
      '<li class="nav-item"><a class="nav-link" href="' + basePath + 'geografia.html">Geografia</a></li>' +
      '<li class="nav-item dropdown">' +
      '<a class="nav-link dropdown-toggle" href="' + basePath + 'frazioni.html" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Frazioni</a>' +
      '<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">' + dropdownItems + "</div>" +
      "</li>" +
      '<li class="nav-item"><a class="nav-link" href="' + basePath + 'fonti.html">Fonti</a></li>' +
      "</ul>" +
      "</div>" +
      "</div>" +
      "</nav>"
    );
  }

  function renderFooter() {
    return (
      '<footer class="py-5 bg-dark">' +
      '<div class="container">' +
      '<p class="m-0 text-center text-white">Civitella in Pillole &mdash; un progetto personale su Civitella in Val di Chiana</p>' +
      "</div>" +
      "</footer>"
    );
  }

  document.addEventListener("DOMContentLoaded", function () {
    var basePath = document.body.getAttribute("data-base-path") || "";
    var navPlaceholder = document.getElementById("navbar-placeholder");
    var footerPlaceholder = document.getElementById("footer-placeholder");
    if (navPlaceholder) {
      navPlaceholder.innerHTML = renderNavbar(basePath);
    }
    if (footerPlaceholder) {
      footerPlaceholder.innerHTML = renderFooter();
    }
  });
})();
