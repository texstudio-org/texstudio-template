# LaTeX Template for Computer Science Research Papers

### A style-agnostic LaTeX template that eliminates the need to write style-specific code and eases switching between the typical document classes of computer science research papers.
###### The template supports *IEEEtran*, *llncs* and *acmart* styles only. Feel free to contribute and support more styles.
---

### Template Structure
* [main.tex](main.tex): the root document of the template. This file *must not* be modified.
* [bibliography](bibliography/): contains bibliography styles and references file. Only the references file shall be modified.
* [config](config/): contains style-specific code and configurations. The contents of this directory *must not* be modified.
* [sections](sections/): directory to add paper sections and text.
* [user](user/): contains user-defined variables and configurations such as paper title, abstract, athors, and packages.
---

### Usage
To write a paper, you only need to add your content in tex files under the [*sections*](sections) directory.
It is recommended to write each section in separate tex file, but the template works perfectly fine if you write all content in one file only.


Specify template settings in [*settings.tex*](user/settings.tex). Set the style to be used (i.e., acm, ieee or llncs) as well as the sections to be included from the [sections](sections) directory. Note that the sections must be added in the same order you want them to appear.

Example:

	\def \varStyle{llncs}
	\def \varSections{introduction,conclusion}


Use the [*topmatter.tex*](user/topmatter.tex) file to define the title, authors, abstract, and keywords.

Example:

    \addTitle{insert title here}
    \addAuthor{Author}{1}
    \addInstitution{Department, Institution}{City}{Country}{{name.surname}@example.com}
    \addAbstract{insert abstract here}
    \addKeywords{insert, comma-separated, keywords, here}

Note that you only need to insert/modify the arguments of the above commands.


Use [*packages.tex*](user/packages.tex) and [*preamble.tex*](user/preamble.tex) to add packages and user-defined preabmle code (e.g., listings, acronyms) respectively.


Finally, use [*references.bib*](bibliography/references.bib) for your bibliography.

---
### Attributions
Below you can find the links to the llncs, acmart and IEEEtran styles.
* [llncs](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines)
* [acmart](https://www.acm.org/publications/proceedings-template)
* [IEEEtran](https://www.ieee.org/conferences/publishing/templates.html)
---
