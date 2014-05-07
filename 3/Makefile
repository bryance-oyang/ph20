PLOTS = problem1.pdf problem2.pdf problem3.pdf\
problem4.pdf problem5_1.pdf problem5_2.pdf p2_problem1.pdf\
p2_problem2.pdf p2_problem3.pdf p2_problem4.pdf
LATEXDEPS = ps3.tex ducky.sty $(PLOTS)
DATA = $(PLOTS:.pdf=.dat)

pdf/ps3.pdf: $(addprefix latex/, $(LATEXDEPS))
	make -f Makelatex

$(addprefix latex/, $(PLOTS)): $(addprefix data/, $(DATA)) ps3_plot.py
	./ps3_plot.py

$(addprefix data/, $(DATA)): ps3.py
	mkdir -p data
	./ps3.py

clean:
	rm -f $(addprefix latex/, $(PLOTS))
	rm -f $(addprefix data/, $(DATA))
