// Navbar condivisa, iniettata via JS in ogni pagina.
// Il footer invece è scritto nell'HTML da tools/genera_seo.py, così lo leggono anche i crawler senza JavaScript.
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
    { slug: "oliveto", nome: "Oliveto" },
    { slug: "pieve-a-maiano", nome: "Pieve a Maiano" },
    { slug: "pieve-al-toppo", nome: "Pieve al Toppo" },
    { slug: "ponticino", nome: "Ponticino" },
    { slug: "spoiano", nome: "Spoiano" },
    { slug: "tegoleto", nome: "Tegoleto" },
    { slug: "tuori", nome: "Tuori" },
    { slug: "viciomaggio", nome: "Viciomaggio" },
    { slug: "borghi-minori", nome: "Borghi e località minori" }
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
    function dropdownItem(href, label, file) {
      var activeCls = current === file ? " active" : "";
      return '<a class="dropdown-item' + activeCls + '" href="' + href + '">' + label + "</a>";
    }
    var divider = '<div class="dropdown-divider"></div>';
    var frazioniItems = FRAZIONI.filter(function (f) { return f.slug !== "borghi-minori"; }).map(function (f) {
      return dropdownItem(basePath + "frazioni/" + f.slug + ".html", f.nome, f.slug + ".html");
    });
    var dropdownItems = [dropdownItem(basePath + "frazioni.html", "Tutte le frazioni", "frazioni.html"), divider]
      .concat(frazioniItems)
      .concat([divider, dropdownItem(basePath + "frazioni/borghi-minori.html", "Borghi e località minori", "borghi-minori.html")])
      .join("\n");

    function navCls(file) {
      return "nav-link" + (current === file ? " active" : "");
    }

    var frazioniActive = inFrazioniFolder() || current === "frazioni.html";

    return (
      '<nav class="navbar navbar-expand-xl navbar-dark bg-dark">' +
      '<div class="container px-lg-5">' +
      '<a class="navbar-brand" href="' + basePath + 'index.html">Civitella in Pillole</a>' +
      '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>' +
      '<div class="collapse navbar-collapse" id="navbarSupportedContent">' +
      '<ul class="navbar-nav ms-auto mb-2 mb-xl-0">' +
      '<li class="nav-item"><a class="' + navCls("index.html") + '" href="' + basePath + 'index.html">Home</a></li>' +
      '<li class="nav-item"><a class="' + navCls("storia.html") + '" href="' + basePath + 'storia.html">Storia</a></li>' +
      '<li class="nav-item"><a class="' + navCls("geografia.html") + '" href="' + basePath + 'geografia.html">Geografia</a></li>' +
      '<li class="nav-item dropdown">' +
      '<a class="nav-link dropdown-toggle' + (frazioniActive ? " active" : "") + '" href="' + basePath + 'frazioni.html" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Frazioni</a>' +
      '<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">' + dropdownItems + "</div>" +
      "</li>" +
      '<li class="nav-item"><a class="' + navCls("patrimonio.html") + '" href="' + basePath + 'patrimonio.html">Patrimonio</a></li>' +
      '<li class="nav-item"><a class="' + navCls("lavoro-e-sapori.html") + '" href="' + basePath + 'lavoro-e-sapori.html" title="Lavoro e sapori">Economia</a></li>' +
      '<li class="nav-item"><a class="' + navCls("feste-e-associazioni.html") + '" href="' + basePath + 'feste-e-associazioni.html" title="Feste e associazioni">Feste</a></li>' +
      '<li class="nav-item"><a class="' + navCls("amministrazione.html") + '" href="' + basePath + 'amministrazione.html">Amministrazione</a></li>' +
      '<li class="nav-item"><a class="' + navCls("fonti.html") + '" href="' + basePath + 'fonti.html">Fonti</a></li>' +
      '<li class="nav-item wm-nav-quiz-item"><a class="' + navCls("quiz.html") + ' wm-nav-quiz" href="' + basePath + 'quiz.html"><i class="bi bi-patch-question"></i>Quiz</a></li>' +
      "</ul>" +
      "</div>" +
      "</div>" +
      "</nav>"
    );
  }

  document.addEventListener("DOMContentLoaded", function () {
    var basePath = document.body.getAttribute("data-base-path") || "";
    var navPlaceholder = document.getElementById("navbar-placeholder");
    if (navPlaceholder) {
      navPlaceholder.innerHTML = renderNavbar(basePath);
    }
  });
})();
