var pictures = document.querySelectorAll('#pictures .image');
var currentPicture = 0;
var pictureInterval = setInterval(nextImage,2000);

function nextImage(){
    pictures[currentPicture].className = 'image';
    currentPicture = (currentPicture+1)%pictures.length;
    pictures[currentPicture].className = 'image showing';
}
