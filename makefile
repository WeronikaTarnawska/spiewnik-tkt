all:
	pdflatex spiewnik.tex < enters.txt > err.txt 2> err.txt

sort:
	cp spiewnik.tex in.tex
	python3 sorter.py

clean:
	rm *.aux *.log *.out *.toc