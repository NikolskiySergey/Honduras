var sliders = document.querySelectorAll('#sliders .view');
var currentSlider = 0;
var slideInterval = setInterval(nextSlider,2000);

function nextSlider(){
    sliders[currentSlider].className = 'view';
    currentSlider = (currentSlider+1)%sliders.length;
    sliders[currentSlider].className = 'view showing';
}
