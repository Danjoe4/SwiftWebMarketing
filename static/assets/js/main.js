(function() {
    
    "use strict";
    
    //===== Prealoder

    window.onload = function() {
        window.setTimeout(fadeout, 500);
    }

    function fadeout() {
        document.querySelector('.preloader').style.opacity = '0';
        document.querySelector('.preloader').style.display = 'none';
    }

    
    /*=====================================
    Sticky
    ======================================= */
    window.onscroll = function () {
        var header_navbar = document.getElementById("header_navbar");
        var logo = document.querySelector("img#logo");
        var sticky = header_navbar.offsetTop;

        if (window.pageYOffset > sticky) {
            header_navbar.classList.add("sticky");
            logo.setAttribute("src", "static/assets/images/logo-2.svg")
        } else {
            header_navbar.classList.remove("sticky");
            logo.setAttribute("src", "static/assets/images/logo.svg")
        }



        // show or hide the back-top-top button
        var backToTo = document.querySelector(".back-to-top");
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            backToTo.style.display = "block";
        } else {
            backToTo.style.display = "none";
        }
    };

    // Get the navbar


    // for menu scroll 
    var pageLink = document.querySelectorAll('.page-scroll');
    
    pageLink.forEach(elem => {
        elem.addEventListener('click', e => {
            e.preventDefault();
            document.querySelector(elem.getAttribute('href')).scrollIntoView({
                behavior: 'smooth',
                offsetTop: 1 - 60,
            });
        });
    });

    // section menu active
    function onScroll(event) {
        var sections = document.querySelectorAll('.page-scroll');
        var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;

        for (var i = 0; i < sections.length; i++) {
            var currLink = sections[i];
            var val = currLink.getAttribute('href');
            var refElement = document.querySelector(val);
            var scrollTopMinus = scrollPos + 73;
            if (refElement.offsetTop <= scrollTopMinus && (refElement.offsetTop + refElement.offsetHeight > scrollTopMinus)) {
                document.querySelector('.page-scroll').classList.remove('active');
                currLink.classList.add('active');
            } else {
                currLink.classList.remove('active');
            }
        }
    };

    window.document.addEventListener('scroll', onScroll);


    //===== close navbar-collapse when a  clicked
    let navbarToggler = document.querySelector(".navbar-toggler");    
    var navbarCollapse = document.querySelector(".navbar-collapse");

    document.querySelectorAll(".page-scroll").forEach(e =>
        e.addEventListener("click", () => {
            navbarToggler.classList.remove("active");
            navbarCollapse.classList.remove('show')
        })
    );
    
})();

//=====  Contact Form 
const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

const alert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible fade show" role="alert">`,
    `   <div>${message}</div>`,
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

// actual send action

function SubForm (formData){
    // send data to server
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', '/email');
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200) {
                var response = '';
                try {
                    response = JSON.parse(this.responseText);
                } catch (err) {
                    response = this.responseText;
                }
                console.log('got response', response);
            }
        }
    };
    console.log('sending data');
    xhttp.send(JSON.stringify(formData));
}



const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    
    console.log('clicked');
    // alert if the form is valid
    formData = {
        'name'    : document.querySelector('input[name="name"]').value,
        'email'   : document.querySelector('input[name="email"]').value,
        'number'   : document.querySelector('input[name="number"]').value,
        'subject' : document.querySelector('input[name="subject"]').value,
        'message' : document.querySelector('textarea[name="message"]').value
    };

    if (formData['name'] && formData['email'] && formData['number'] && formData['subject'] && 
    formData['message'] && alertPlaceholder.innerHTML == '') {
        SubForm(formData);
        alert('Your message has been sent. A member of our team will email you shortly', 'success')
        // clear the form
        document.querySelector('input[name="name"]').value = '';
        document.querySelector('input[name="email"]').value = '';
        document.querySelector('input[name="number"]').value = '';
        document.querySelector('input[name="subject"]').value = '';
        document.querySelector('textarea[name="message"]').value = '';

        // wait 5 seconds and dismiss the alert
        setTimeout(() => {
            alertPlaceholder.innerHTML = '';
            }, 5000)
    }
    else if (alertPlaceholder.innerHTML == '') {
        alert('Please fill out all the fields', 'danger')
        setTimeout(() => {
            alertPlaceholder.innerHTML = '';
            }, 2000)
    }
  })
}