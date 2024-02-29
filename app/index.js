window.addEventListener('load', async function () {
  const video = document.getElementById('js-video');
  const table = document.getElementById('js-table');

  const response = await fetch('./audio_metadata.json')
  const metadata = await response.json()

  for (const [index, data] of metadata.entries()) {
    const row = document.createElement('tr');

    let cell = document.createElement('td');
    cell.textContent = index;
    row.appendChild(cell);

    for (const key in data) {
      let cell = document.createElement('td');
      cell.textContent = Math.floor(data[key]);
      row.appendChild(cell);
    }
    table.appendChild(row);

    data.hasPlayed = false;
  }

  console.table(metadata);


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

      if (diff < -1 && data.hasPlayed) {
        data.hasPlayed = false;
      }

      if (0 < diff && diff < 0.5 && !data.hasPlayed) {
        console.info(index, data, diff);
        data.hasPlayed = true;
        playAudioAfterVideo(index)
      };
    };
  });
})
