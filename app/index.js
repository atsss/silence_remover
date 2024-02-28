(async function () {
  const response = await fetch('./audio_metadata.json')
  const metadata = await response.json()
  console.table(metadata);

  const video = document.getElementById('js-video');

  function playAudioAfterVideo(index) {
    video.pause()
    const audio = document.createElement('audio');
    audio.src = `./assets/active-${index}.wav`;
    audio.addEventListener('ended', function() {
        video.play();
    });
    audio.play();
  }

  video.addEventListener('timeupdate', function(event) {
    const currentTime = event.target.currentTime;
    for (const [index, data] of metadata.entries()) {
      const diff = Math.floor(currentTime*10)/10 - data['start_sec']
      if (0 < diff && diff < 0.35) {
        console.info(index, data, diff);
        playAudioAfterVideo(index)
      };
    };
  });
}());
