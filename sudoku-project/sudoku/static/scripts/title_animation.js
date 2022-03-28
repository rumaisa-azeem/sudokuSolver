var textWrapper = document.querySelector(".ml6 .letters");
textWrapper.innerHTML = textWrapper.textContent.replace(
	/\S/g,
	"<span class='letter'>$&</span>"
);

document
	.getElementById("animateHeading")
	.addEventListener("mouseover", animateHeading);

function animateHeading(event) {
	anime.timeline().add({
		targets: ".ml6 .letter",
		translateY: ["1.1em", 0],
		translateZ: 0,
		duration: 750,
		delay: (el, i) => 50 * i
	});
}

