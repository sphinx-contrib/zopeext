# -*- coding: utf-8 -*-
import os
import sys

import pytest

# Add current directory to path so we can import the example.py file.
sys.path.insert(0, os.path.abspath(__file__))

pytest_plugins = "sphinx.testing.fixtures"


@pytest.mark.sphinx(
    "html",
    srcdir=os.path.join(os.path.dirname(__file__), "examples"),
)
@pytest.mark.skip(reason="Test needs updating.")
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / "index.html").read_text()

    for _n, _E in enumerate(_EXPECTED):
        assert _E.strip() in html


_EXPECTED = [
    """
<script>
$(document).ready(function() {
  $('.interface').addClass('class');
});
</script>
""",
    """
  <div class="section" id="the-example-module">
<h1>The <a class="reference internal" href="#module-example" title="example"><code class="xref py py-mod docutils literal notranslate"><span class="pre">example</span></code></a> Module<a class="headerlink" href="#the-example-module" title="Permalink to this headline">¶</a></h1>
<p>Here is a reference to the Interface: <a class="reference internal" href="#example.IMyInterface" title="example.IMyInterface"><code class="xref py py-interface docutils literal notranslate"><span class="pre">example.IMyInterface</span></code></a>, and to the
implementation: <a class="reference internal" href="#example.MyImplementation" title="example.MyImplementation"><code class="xref py py-class docutils literal notranslate"><span class="pre">example.MyImplementation</span></code></a>.</p>
<table class="longtable docutils align-default">
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="#module-example" title="example"><code class="xref py py-obj docutils literal notranslate"><span class="pre">example</span></code></a></p></td>
<td><p>Example module using <code class="xref py py-mod docutils literal notranslate"><span class="pre">zope.interface</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#example.IMyInterface" title="example.IMyInterface"><code class="xref py py-obj docutils literal notranslate"><span class="pre">example.IMyInterface</span></code></a>(x)</p></td>
<td><p>This is an example of an interface.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#example.MyImplementation" title="example.MyImplementation"><code class="xref py py-obj docutils literal notranslate"><span class="pre">example.MyImplementation</span></code></a>(x[, y])</p></td>
<td><p>Example</p></td>
</tr>
</tbody>
</table>
<span class="target" id="module-example"></span><p>Example module using <code class="xref py py-mod docutils literal notranslate"><span class="pre">zope.interface</span></code>.</p>
<p>Here we define an interface <a class="reference internal" href="#example.IMyInterface" title="example.IMyInterface"><code class="xref py py-interface docutils literal notranslate"><span class="pre">IMyInterface</span></code></a> and an
implementation <a class="reference internal" href="#example.MyImplementation" title="example.MyImplementation"><code class="xref py py-class docutils literal notranslate"><span class="pre">MyImplementation</span></code></a>.</p>
""",
    """
<dl class="py interface">
<dt class="sig sig-object py" id="example.IMyInterface">
<em class="property"><span class="pre">interface</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="example.IMyInterface.x">
<span class="sig-name descname"><span class="pre">x</span></span><a class="headerlink" href="#example.IMyInterface.x" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="example.IMyInterface.equals">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</dd></dl>

</dd></dl>""",
    """
<dl class="py interface">
<dt class="sig sig-object py" id="example.IMySecondInterface">
<em class="property"><span class="pre">interface</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMySecondInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMySecondInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>A refinement of the previous interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="example.IMySecondInterface.y">
<span class="sig-name descname"><span class="pre">y</span></span><a class="headerlink" href="#example.IMySecondInterface.y" title="Permalink to this definition">¶</a></dt>
<dd><p>A new required attribute</p>
</dd></dl>

</dd></dl>""",
    """
<dl class="py class">
<dt class="sig sig-object py" id="example.MyImplementation">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">MyImplementation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation" title="Permalink to this definition">¶</a></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt class="sig sig-object py" id="example.MyImplementation.equals">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
</dd></dl>

</dd></dl>""",
    """
<li><p>Here is an explicit example of <cite>autointerface</cite></p>
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="pre">interface</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
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
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</dd></dl>

</dd></dl>""",
    """
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="pre">interface</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMySecondInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Bases: <a class="reference internal" href="#example.IMyInterface" title="example.IMyInterface"><code class="xref py py-class docutils literal notranslate"><span class="pre">example.IMyInterface</span></code></a></p>
<p>A refinement of the previous interface.</p>
<dl class="py attribute">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">y</span></span></dt>
<dd><p>A new required attribute</p>
</dd></dl>

</dd></dl>""",
    """
<li><p>Now the interface with explicit members.</p>
<dl class="py interface">
<dt class="sig sig-object py">
<em class="property"><span class="pre">interface</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">IMyInterface</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<dl class="py method">
<dt class="sig sig-object py" id="example.IMyInterface.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">kw</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.IMyInterface.__init__" title="Permalink to this definition">¶</a></dt>
<dd><p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
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
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</dd></dl>

</dd></dl>

</li>""",
    """
<li><p>Now the class with explicit members.</p>
<dl class="py class">
<dt class="sig sig-object py">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">example.</span></span><span class="sig-name descname"><span class="pre">MyImplementation</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt class="sig sig-object py" id="example.MyImplementation.__init__">
<span class="sig-name descname"><span class="pre">__init__</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">y</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.0</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#example.MyImplementation.__init__" title="Permalink to this definition">¶</a></dt>
<dd><p>Constructor.</p>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
<dt>y<span class="classifier">float, optional</span></dt><dd><p>An additional  parameter <cite>y</cite> that is not part of the interface, but which
has a default value (3.0) and so does not violate the interface definition.</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py">
<span class="sig-name descname"><span class="pre">equals</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<dl class="simple">
<dt>x<span class="classifier">float</span></dt><dd><p>The parameter <cite>x</cite>.</p>
</dd>
</dl>
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

</li>""",
]
