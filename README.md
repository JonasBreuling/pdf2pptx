# pdf2pptx - seamless conversion of pdf files to PowerPoint presentations

<p align="center">
<a href="https://img.shields.io/badge/License-BSD_3--Clause-blue.svg"><img alt="License: BSD 3" src="https://img.shields.io/badge/License-BSD_3--Clause-blue.svg"></a>
<!-- <a href="https://pypi.org/project/scipy_dae/"><img alt="PyPI" src="https://img.shields.io/pypi/v/scipy_dae"></a> -->
</p>

Convert pdf files to PowerPoint presentatins using a single command.

## Installation

```bash
python -m pip install .
```

## Basic usage

Convert `presentation.pdf` to `slides.pptx` using 400 dots per inch.

```bash
python -m pdf2pptx -dpi=400 presentation/presentation.pdf -out=presentation/slides.pptx
```
