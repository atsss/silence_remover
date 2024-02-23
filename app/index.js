fetch('./audio_metadata.json')
    .then((response) => response.json())
    .then((json) => {
      const $container = $('.js-audio-list')
      for(const [index, data] of json.entries()) {
        const child = $(`<div><div>${data["start_sec"]} - ${data["end_sec"]}</div><audio controls><source src="./assets/active-${index}.wav"></audio></div>`);
        $container.append(child);
      }
    });
