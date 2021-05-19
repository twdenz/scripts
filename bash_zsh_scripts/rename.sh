#!/usr/bin/bash

read -p "Which file extension do you want to change: " file_extension
read -p "What do you want to change: " from
read -p "What do you want to change it into: " to

for file in *.$file_extension; do
	if [[ "$file" != "${file/$from/$to}" ]]; then 
			mv "$file" "${file/$from/$to}";
		else echo "${file} and "${file/$from/$to}" where the same"
	fi
done


