lua:
	cp spiewnik.tex spiewnik-tkt-2024.tex
	lualatex -interaction=nonstopmode spiewnik-tkt-2024.tex > err.txt

pdf:
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error spiewnik.tex > err.txt 2> err.txt

sort:
	cp spiewnik.tex in.tex
	python3 sorter.py

clean:
	rm *.aux *.log *.out *.toc *.fdb_latexmk *.fls err.txt