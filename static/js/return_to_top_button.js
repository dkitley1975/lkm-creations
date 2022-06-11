//Get the button:
const rttbutton = document.getElementById("rtt-link");

// When the user scrolls down 300px from the top of the document,
// show the button
window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
	if (
		document.body.scrollTop > 300 ||
		document.documentElement.scrollTop > 300
	) {
		rttbutton.style.display = "block";
	} else {
		rttbutton.style.display = "none";
	}
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	document.body.scrollTop = 0; // For Safari
	document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
