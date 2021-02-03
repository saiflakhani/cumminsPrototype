var meow = null
var currentVideo = 0;
var videos = null;
var m_devices = null;
$(document).ready(function () {
    var domain = "katherine-video-calling.ga";
    var options = {
        roomName: "saif",
        width: 700,
        height: 700,
        parentNode: document.querySelector('#meet')
    }
    meow = new JitsiMeetExternalAPI(domain, options);
});

function switchVideo(){
    meow.getAvailableDevices().then(devices => {
        m_devices = devices;
        videos = devices['videoInput'].length;
        console.log(devices);
        console.log(videos);
        console.log(currentVideo);
        currentVideo = currentVideo+1;
        meow.setVideoInputDevice(devices['videoInput'][(currentVideo)%videos]['label'], devices['videoInput'][(currentVideo)%videos]['deviceId']);
    });
}

