#!/bin/bash
for ((i=1; i<4; i++)) {
	for ((j=1; j<7; j++)) {
		cat "${i}-${j}".txt >> "${i}".txt
	}
}