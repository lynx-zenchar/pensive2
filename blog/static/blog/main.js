document.getElementById('readMoreButton').addEventListener('click', function() {
  var moreText = document.getElementById('moreText');
  if (moreText.style.display === "none") {
    moreText.style.display = "block";
  } else {
    moreText.style.display = "none";
  }
});
