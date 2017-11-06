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

	if (true) {
		$('#submitButtonContainer').show('slide', {direction: 'right'}, 1000);
		$('.submitButton').click(submitted);
	}
}

function submitted(){
	
	$('#submitButtonContainer').hide('slide', {direction: 'right'}, 1000);
}



function initializeBoard(rows) {
	let board = new Array(rows);
	for (let i = 0; i < rows; i++){
		board[i] = new Array(4);
	}
	return board;
}

////////Code
function main(){
	
}


// global variables
let round = 0;
let board = initializeBoard(12);
//control of one round
window.addEventListener('load', dragDropFunctionality, false);







