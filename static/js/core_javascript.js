// document.addEventListener("DOMContentLoaded", function () {
// 	const navbar_autohide = document.querySelector(".autohide");

// 	// adds padding-top to the body (if necessary)
// 	const navbar_height = document.querySelector(".navbar").offsetHeight;
// 	document.body.style.paddingTop = navbar_height + "px";

// 	if (navbar_autohide) {
// 		var last_scroll_top = 0;
// 		window.addEventListener("scroll", function () {
// 			let scroll_top = window.scrollY;
// 			if (scroll_top < last_scroll_top) {
// 				navbar_autohide.classList.remove("scrolled-down");
// 				navbar_autohide.classList.add("scrolled-up");
// 			} else {
// 				navbar_autohide.classList.remove("scrolled-up");
// 				navbar_autohide.classList.add("scrolled-down");
// 			}
// 			last_scroll_top = scroll_top;
// 		});
// 	}
// });
