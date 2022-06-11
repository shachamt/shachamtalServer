
//fill progress
var gvalue = 1;
function fillProgress() {
  var progressFill = document.getElementById('loadProgress');
  setInterval(function () {
    if (gvalue < 100) {
      gvalue++;
      progressFill.value = gvalue;
    }
    fillProgress();
  }, 1000);
  if (gvalue == 100) {
    var message = document.getElementById('allLoad');
    message.innerText = 'All load! You can send the file now by clicking the button'
  }
}

//read more
const readMoreBtn = document.querySelector('.readMoreButton');
const text = document.querySelector('.text');
readMoreBtn.addEventListener('click', (e) => {
  text.classList.toggle('showMore');
  if (readMoreBtn.innerText === 'Read More') {
    readMoreBtn.innerText = 'Read Less';
  } else {
    readMoreBtn.innerText = 'Read More';
  }
})

//show what page I am on
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/
const navLinks = document.querySelectorAll('nav a').forEach(link => {
  if (link.href.includes(`${activePage}`)) {
    link.classList.add('active');
  }
});

//form validation
const fullName = document.getElementById("fullName")
const form = document.getElementById("myForm")
const error = document.getElementById("error")
const email = document.getElementById("email")

form.addEventListener('submit', (e) => {
    let messages = []

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))) {
      messages.push ('Email is not valid')
    }

    if(fullName.value.length <2) {
        messages.push ('Full name must be at least 2 characters')
    }

    if (messages.length>0) {
        e.preventDefault()
        error.innerText = messages.join (', ')
    }

})


