let table = "";
const sequencia = JSON.parse(document.getElementById('task_result').textContent)
console.log('teste')
for (let i = 0; i < sequencia.length ; i++) {
  table +="<tr>"
    for (let j = 0; j < sequencia[i].length ; j++) {

        if (sequencia[i][j] === "A") {
            table += `<td style="color: #4bd4ff; font-weight:bold;"> ${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "B") {
            table += `<td style="color: #f50707; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "C") {
            table += `<td style="color: #ffe050; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "D") {
            table += `<td style="color: #d900ff; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "E") {
            table += `<td style="color: #1900a8; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "F") {
            table += `<td style="color: #ff9500; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "G") {
            table += `<td style="color: #776d43; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "H") {
            table += `<td style="color: #f3ff6b; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "I") {
            table += `<td style="color: #8ea24e; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "K") {
            table += `<td style="color: #7dff03; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "L") {
            table += `<td style="color: #0c6600; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "M") {
            table += `<td style="color: #438c49; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "N") {
            table += `<td style="color: #a0610e; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "P") {
            table += `<td style="color: #4d8a7d; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "Q") {
            table += `<td style="color: #03fcc7; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "R") {
            table += `<td style="color: #10b0b5; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "S") {
            table += `<td style="color: #036791; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "T") {
            table += `<td style="color: #65adf0; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "V") {
            table += `<td style="color: #8f5dde; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "W") {
            table += `<td style="color: #6300ff; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "X") {
            table += `<td style="color: #6300ff; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "Y") {
            table += `<td style="color: #8572a3; font-weight:bold;">${sequencia[i][j]}</td>`
        } else if (sequencia[i][j] === "-"){
            table += `<td style="color: #b50baf; font-weight:bold;">${sequencia[i][j]}</td>`
        }

    }
    table += "</tr>"
    document.getElementById("result_sequencia").innerHTML = table
}

function myFunction() {
  /* Get the text field */
  var copyText = document.getElementById("copy");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

}
