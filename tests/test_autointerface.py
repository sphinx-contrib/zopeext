# -*- coding: utf-8 -*-
import os
from packaging import version
import re
import shutil
import sys

import sphinx
if sphinx.version_info < (7, 2):
    from sphinx.testing.path import path as Path
else:
    from pathlib import Path
    
import pytest

# Add current directory to path so we can import the example.py file.
sys.path.insert(0, os.path.abspath(__file__))

pytest_plugins = "sphinx.testing.fixtures"

_SRCDIR = Path(os.path.dirname(__file__)) / "examples"
_BUILDDIR = _SRCDIR / '_build{}'.format(os.environ.get('NOX_CURRENT_SESSION', ''))

@pytest.mark.sphinx(
    "html",
    srcdir=_SRCDIR,
    builddir=_BUILDDIR,
)
@pytest.mark.skipif(version.parse(sphinx.__version__) <= version.parse("4.5.0"),
                    reason="Need customized tests for Sphinx 4.5.0.")
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / "index.html").read_text()

    for _n, _E in enumerate(_EXPECTED):
        # Changes for backwards compatibility
        _E = _E.strip()
        if version.parse(sphinx.__version__) < version.parse("7.2.0"):
            _E = _E.replace("Link", "Permalink")
            
        if version.parse(sphinx.__version__) < version.parse("8.2.0"):
            # Note `(.*?)` is a non-greedy match.
            p = re.compile(r'<span class="k"><span class="pre">(.*?)</span></span>')
            r = r'<span class="pre">\1</span>'
            if p.search(_E):
                _E = p.sub(r, _E)
        
        if version.parse(sphinx.__version__) >= version.parse("9.0.0"):
            p = re.compile(r'<em class="property">(.*?)</em>')
            r = r'<span class="property">\1</span>'
            if p.search(_E):
                _E = p.sub(r, _E)
            
        try:
            assert _E in html
        except:
            raise
            # with open('_lhs.html', 'w') as f:
            #     f.write(_E)
            # with open('_rhs.html', 'w') as f:
            #     f.write(html)
            # raise
    
    # This should leave broken builds, but remove the rest.
    shutil.rmtree(app.outdir.parent, ignore_errors=True)

_EXPECTED = [
    """
<script>
$(document).ready(function() {
  $('.interface').addClass('class');
});
</script>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py" id="example.IMyInterface">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface" title="Link to this definition">¶</a></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="example.IMyInterface.x">
<span class="sig-name descname"><span class="pre">x</span></span><a class="headerlink" href="#example.IMyInterface.x" title="Link to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>
""",
    """
<dl class="py method">
<dt class="sig sig-object py" id="example.IMyInterface.equals">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface.equals" title="Link to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<section id="parameters">
<h2>Parameters<a class="headerlink" href="#parameters" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py" id="example.IMySecondInterface">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMySecondInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMySecondInterface" title="Link to this definition">¶</a></dt>
<dd><p>A refinement of the previous interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="example.IMySecondInterface.y">
<span class="sig-name descname"><span class="pre">y</span></span><a class="headerlink" href="#example.IMySecondInterface.y" title="Link to this definition">¶</a></dt>
<dd><p>A new required attribute</p>
</dd></dl>""",
    """
<dl class="py class">
<dt class="sig sig-object py" id="example.MyImplementation">
<em class="property"><span class="k"><span class="pre">class</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">MyImplementation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation" title="Link to this definition">¶</a></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt class="sig sig-object py" id="example.MyImplementation.equals">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation.equals" title="Link to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<section id="id1">
<h2>Parameters<a class="headerlink" href="#id1" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">_a</span></span></dt>
<dd><p>A private required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">x</span></span></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<section id="id2">
<h2>Parameters<a class="headerlink" href="#id2" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
<section id="id3">
<h2>Notes<a class="headerlink" href="#id3" title="Link to this heading">¶</a></h2>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</section>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMySecondInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A refinement of the previous interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">y</span></span></dt>
<dd><p>A new required attribute</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">class</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">MyImplementation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<section id="id4">
<h2>Parameters<a class="headerlink" href="#id4" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">x</span></span></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<section id="id5">
<h2>Parameters<a class="headerlink" href="#id5" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
<section id="id6">
<h2>Notes<a class="headerlink" href="#id6" title="Link to this heading">¶</a></h2>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</section>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMySecondInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Bases: <a class="reference internal" href="#example.IMyInterface" title="example.IMyInterface"><code class="xref py py-class docutils literal notranslate"><span class="pre">example.IMyInterface</span></code></a></p>
<p>A refinement of the previous interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">y</span></span></dt>
<dd><p>A new required attribute</p>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">interface</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py method">
<dt class="sig sig-object py" id="example.IMyInterface.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">kw</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface.__init__" title="Link to this definition">¶</a></dt>
<dd><p>The constructor should set the attribute <cite>x</cite>.</p>
<section id="id7">
<h2>Parameters<a class="headerlink" href="#id7" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">_a</span></span></dt>
<dd><p>A private required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<section id="id8">
<h2>Parameters<a class="headerlink" href="#id8" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
<section id="id9">
<h2>Notes<a class="headerlink" href="#id9" title="Link to this heading">¶</a></h2>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</section>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py class">
<dt class="sig sig-object py">
<em class="property"><span class="k"><span class="pre">class</span></span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">MyImplementation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt class="sig sig-object py" id="example.MyImplementation.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation.__init__" title="Link to this definition">¶</a></dt>
<dd><p>Constructor.</p>
<section id="id10">
<h2>Parameters<a class="headerlink" href="#id10" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
<dt>y<span class="classifier">float, optional</span></dt><dd><p>An additional  parameter <cite>y</cite> that is not part of the interface, but which
has a default value (3.0) and so does not violate the interface definition.</p>
</dd>
</dl>
</section>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<section id="id11">
<h2>Parameters<a class="headerlink" href="#id11" title="Link to this heading">¶</a></h2>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</section>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">x</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span></em></dt>
<dd></dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">y</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span></em></dt>
<dd></dd></dl>

</dd></dl>
""",
]
