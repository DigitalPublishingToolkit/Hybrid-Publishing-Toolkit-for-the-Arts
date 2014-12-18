for %%f in (*.md) do (
	pandoc %%f --latex-engine=xelatex -o %%~nf.pdf
)
