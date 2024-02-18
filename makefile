year=2024

help:
	## lua       lualatex build
	## pdf       pdflatex build (does not support custom font)
	## sort      sort songs from spiewnik.tex, save result in sorted.tex
	## index     generate index, save in index.txt
	## clean     rm *.aux *.log *.out *.toc *.fdb_latexmk *.fls *.txt
	## release   compress spiewnik.pdf, save in spiewnik-tkt-2024.pdf

lua:
	lualatex -interaction=nonstopmode spiewnik.tex > err.txt

pdf:
	pdflatex -interaction nonstopmode -halt-on-error -file-line-error spiewnik.tex > err.txt 2> err.txt

sort:
	python3 sorter.py spiewnik.tex sorted.tex

index:
	python3 index.py

release:
	ps2pdf -dPDFSETTINGS=/printer spiewnik.pdf "spiewnik-tkt-${year}.pdf"

clean:
	rm *.aux *.log *.out *.toc *.fdb_latexmk *.fls *.txt