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
    { slug: "gebbia", nome: "Gebbia" },
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

  function currentFile() {
    var path = window.location.pathname;
    return path.substring(path.lastIndexOf("/") + 1) || "index.html";
  }

  function inFrazioniFolder() {
    return window.location.pathname.indexOf("/frazioni/") !== -1;
  }

  function renderNavbar(basePath) {
    var current = currentFile();
    var dropdownItems = FRAZIONI.map(function (f) {
      var file = f.slug + ".html";
      var activeCls = current === file ? " active" : "";
      return '<a class="dropdown-item' + activeCls + '" href="' + basePath + "frazioni/" + file + '">' + f.nome + "</a>";
    }).join("\n");

    function navCls(file) {
      return "nav-link" + (current === file ? " active" : "");
    }

    var frazioniActive = inFrazioniFolder() || current === "frazioni.html";

    return (
      '<nav class="navbar navbar-expand-lg navbar-dark bg-dark">' +
      '<div class="container px-lg-5">' +
      '<a class="navbar-brand" href="' + basePath + 'index.html">Civitella in Pillole</a>' +
      '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>' +
      '<div class="collapse navbar-collapse" id="navbarSupportedContent">' +
      '<ul class="navbar-nav ms-auto mb-2 mb-lg-0">' +
      '<li class="nav-item"><a class="' + navCls("index.html") + '" href="' + basePath + 'index.html">Home</a></li>' +
      '<li class="nav-item"><a class="' + navCls("storia.html") + '" href="' + basePath + 'storia.html">Storia</a></li>' +
      '<li class="nav-item"><a class="' + navCls("geografia.html") + '" href="' + basePath + 'geografia.html">Geografia</a></li>' +
      '<li class="nav-item"><a class="' + navCls("amministrazione.html") + '" href="' + basePath + 'amministrazione.html">Amministrazione</a></li>' +
      '<li class="nav-item dropdown">' +
      '<a class="nav-link dropdown-toggle' + (frazioniActive ? " active" : "") + '" href="' + basePath + 'frazioni.html" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Frazioni</a>' +
      '<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">' + dropdownItems + "</div>" +
      "</li>" +
      '<li class="nav-item"><a class="' + navCls("fonti.html") + '" href="' + basePath + 'fonti.html">Fonti</a></li>' +
      "</ul>" +
      "</div>" +
      "</div>" +
      "</nav>"
    );
  }

  function renderFooter(basePath) {
    return (
      '<footer class="site-footer py-5">' +
      '<div class="container px-lg-5">' +
      '<div class="row gy-4">' +
      '<div class="col-lg-5">' +
      '<h2 class="fw-bold mb-3">Civitella in Pillole</h2>' +
      '<p class="mb-0" style="color: rgba(255,255,255,.78);">Un progetto personale di raccolta e divulgazione dedicato a Civitella in Val di Chiana, il suo capoluogo storico e le tredici frazioni: storia, geografia, chiese, curiosita\' e tradizioni del territorio.</p>' +
      "</div>" +
      '<div class="col-lg-3">' +
      '<h3 class="fw-bold mb-3">Esplora</h3>' +
      '<ul class="list-unstyled d-flex flex-column gap-2">' +
      '<li><a href="' + basePath + 'storia.html">Storia</a></li>' +
      '<li><a href="' + basePath + 'geografia.html">Geografia</a></li>' +
      '<li><a href="' + basePath + 'amministrazione.html">Amministrazione</a></li>' +
      '<li><a href="' + basePath + 'frazioni.html">Le frazioni</a></li>' +
      "</ul>" +
      "</div>" +
      '<div class="col-lg-4">' +
      '<h3 class="fw-bold mb-3">Trasparenza</h3>' +
      '<p class="mb-2" style="color: rgba(255,255,255,.78);">Non e\' un sito istituzionale del Comune. Tutte le fonti usate sono elencate pubblicamente.</p>' +
      '<a href="' + basePath + 'fonti.html">Vedi le fonti <i class="bi bi-arrow-right"></i></a>' +
      "</div>" +
      "</div>" +
      '<div class="footer-bottom mt-4 pt-4 text-center">Civitella in Pillole &mdash; progetto personale, non affiliato al Comune di Civitella in Val di Chiana</div>' +
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
      footerPlaceholder.innerHTML = renderFooter(basePath);
    }
  });
})();
