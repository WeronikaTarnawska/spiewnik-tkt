all:
	# echo "choose target" 

lua:
	lualatex -interaction=nonstopmode spiewnik.tex > err.txt

pdf:
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error spiewnik.tex > err.txt 2> err.txt

sort:
	python3 sorter.py spiewnik.tex sorted.tex

index:
	# todo

clean:
	rm *.aux *.log *.out *.toc *.fdb_latexmk *.fls err.txt