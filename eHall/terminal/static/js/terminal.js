function setEvent(terminalID, select){
  eventID = select.options[select.selectedIndex].value;
  $.ajax({
    type: 'GET',
    url: '/terminal/event/',
    data: {
      terminal: terminalID,
      event: eventID,
    }

  });
}

function notifyTerminal(terminalID) {
  console.log("notifyTerminal()" + terminalID.id);
  if (terminalID.innerHTML == "Go!") {
    terminalID.innerHTML = "Event closed.";
    setStatus(terminalID.id, true)
  } else {
    terminalID.innerHTML = "Go!";
    setStatus(terminalID.id, false)
  }
  // document.getElementById("id_Event" + terminalID).disabled = true;
}

function setStatus(id, bool){
  $.ajax({
    type: 'GET',
    url: '/terminal/launch/',
    data: {
      id: id,
      bool: bool,
    }

  });
}
