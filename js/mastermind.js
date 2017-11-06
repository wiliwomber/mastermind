"use strict";

// JavaScript Documentr

function dragDropFunctionality(){
	//add drag and drop to color pallete
	let colors = document.getElementsByClassName("color");
	for (let i = 0; i < colors.length; i++){
		colors[i].addEventListener('dragstart', startdrag, false);
		colors[i].addEventListener('dragend', enddrag, false);
		colors[i].addEventListener('drop', handleDrop, false);
	}
	//add drop enter to positions of current round
	for (let i = 0; i < 4; i++) {
		let id = 4*round + i;
		let position = document.getElementById(id);
		position.addEventListener('dragover', elementover, false);
		position.addEventListener('dragenter', enterdrag, false);
		position.addEventListener('dragleave', leavedrag, false);
		position.addEventListener('drop', handleDrop, false);
	}
}


function startdrag(e){
	this.style.opacity = '0.3';
	let dragImage = new Image(25,25);
	dragImage.src = "../images/" + this.getAttribute("id") + ".png";
	dragImage.style.width = '25px';
	dragImage.style.height = '25px';
    let div = document.createElement('div');
    div.appendChild(dragImage);
    div.style.position = "absolute"; div.style.top = "0px";
	div.style.left = "-500px";
	document.querySelector('body').appendChild(div);
	e.dataTransfer.setDragImage(dragImage,13,13);
	e.dataTransfer.setData('text/plain', this.getAttribute('id'));
}


function enddrag(e){
	this.style.opacity = "1";
}


function elementover(e){
	e.preventDefault();
	e.dataTransfer.dropEffect = 'move';
}


function enterdrag(e){
	this.style.backgroundImage = 'url(../images/ondrag.png)';
}


function leavedrag(e){
	if(typeof board[round][this.getAttribute('id')] == 'undefined'){
		this.style.backgroundImage = 'url(../images/hole.png)';
	} else {
		this.style.backgroundImage = 'url(../images/' + board[round][this.getAttribute('id')] + '.png';
	}


}

function handleDrop(e){
	e.preventDefault();
	board[round][this.getAttribute('id')] = e.dataTransfer.getData('text/plain');
	let url = 'url(../images/' + e.dataTransfer.getData('text/plain') + '.png)'
	this.style.backgroundImage = url;
	submit();
}


function submit() {
	let allGuessesSet = true;
	for (let i = 0; i < 4; i++) {
		if (typeof board[round][i] === 'undefined'){
			allGuessesSet = false;
		}
	}
	if (allGuessesSet) {
		$('#submitButtonContainer').show('slide', {direction: 'right'}, 1000);
		$('.submitButton').click(finishRound);
	}
}

function finishRound(){
	$('#submitButtonContainer').hide('slide', {direction: 'right'}, 1000);
	generateFeedback();
}



function initializeBoard(rows) {
	let board = new Array(rows);
	for (let i = 0; i < rows; i++){
		board[i] = new Array(4);
	}
	return board;
}

function generateScode(){
	let scode = new Array(4);
	let availableColors = ['purple','blue','green','yellow','orange','red'];
	for (let i = 0; i < 4; i++){
		scode[i] = availableColors[(Math.floor(Math.random() * 5))];
		console.log(scode[i])
	}
	return scode;
}
function generateFeedback(){
	let rightPlace = 0;
	let rightColor = 0;
	//create temp arrays to compare witheach other
	let tempScode = scode.slice(0);
	let currentRow = new Array(4);
	for (let i = 0; i < 4; i++){
		currentRow[i] = board[round][i];
		console.log(currentRow[i]);
	}
/*
    # Check if right positions are given
    for i in range(4):
        # comparison goes backwards so that wont point out of index
        if row_scode[3-i] == row_given[3-i]:
            right_place += 1
            row_given.pop(3-i)
            row_scode.pop(3-i)

    # Check if right colors are on the board
    for color_given in row_given:
        m = 0
        for color_scode in row_scode:
            if color_scode == color_given:
                right_color += 1
                row_scode.pop(m)
                break
            m += 1

    # Create feedback string
    feedback = []
    for i in range(right_place):
        feedback.append("black")
    for i in range(right_color):
        feedback.append("white")

    # Check whether final solution was found
    return feedback
------
'''
*/
}

////////Code
function main(){
window.addEventListener('load', dragDropFunctionality, false);
}


// global variables
let round = 0;
let board = initializeBoard(12);
let scode = generateScode();
//control of one round
main();
