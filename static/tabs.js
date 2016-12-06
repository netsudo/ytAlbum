function reset() {
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tabcontent.length; i++) {
        tablinks[i].classList.remove("active");
    }
}

function openTab(evt, tabLink) {
    reset();

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(tabLink).style.display = "block";
    evt.currentTarget.classList.add("active");

}


function init() {
    reset();

    document.getElementsByClassName("tabcontent")[0].style.display = "block";
    document.getElementsByClassName("tablinks")[0].classList.add("active");

  }
  window.onload = init;
