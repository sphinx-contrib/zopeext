# -*- coding: utf-8 -*-
import os

from zope.interface import Interface, Attribute

import pytest

pytest_plugins = "sphinx.testing.fixtures"


@pytest.mark.sphinx(
    "html",
    srcdir=os.path.join(os.path.dirname(__file__), "examples"),
)
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / "index.html").read_text()

    for _n, _E in enumerate(_EXPECTED):
        assert _E.strip() in html


_EXPECTED = [
    """
  <div class="section" id="the-example-module">
<h1>The <code class="xref py py-mod docutils literal notranslate"><span class="pre">example</span></code> Module<a class="headerlink" href="#the-example-module" title="Permalink to this headline">¶</a></h1>
<table class="longtable docutils align-default">
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="#module-sphinxcontrib.zopeext.example" title="sphinxcontrib.zopeext.example"><code class="xref py py-obj docutils literal notranslate"><span class="pre">sphinxcontrib.zopeext.example</span></code></a></p></td>
<td><p>Examples using <code class="xref py py-mod docutils literal notranslate"><span class="pre">zope.interface</span></code>.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="#sphinxcontrib.zopeext.example.IMyInterface" title="sphinxcontrib.zopeext.example.IMyInterface"><code class="xref py py-obj docutils literal notranslate"><span class="pre">sphinxcontrib.zopeext.example.IMyInterface</span></code></a>(x)</p></td>
<td><p>This is an example of an interface.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="#sphinxcontrib.zopeext.example.MyImplementation" title="sphinxcontrib.zopeext.example.MyImplementation"><code class="xref py py-obj docutils literal notranslate"><span class="pre">sphinxcontrib.zopeext.example.MyImplementation</span></code></a>(x)</p></td>
<td><p>Example</p></td>
</tr>
</tbody>
</table>
<span class="target" id="module-sphinxcontrib.zopeext.example"></span><p>Examples using <code class="xref py py-mod docutils literal notranslate"><span class="pre">zope.interface</span></code>.</p>
<p>Here we define an interface <a class="reference internal" href="#sphinxcontrib.zopeext.example.IMyInterface" title="sphinxcontrib.zopeext.example.IMyInterface"><code class="xref py py-class docutils literal notranslate"><span class="pre">IMyInterface</span></code></a> and an
implementation <a class="reference internal" href="#sphinxcontrib.zopeext.example.MyImplementation" title="sphinxcontrib.zopeext.example.MyImplementation"><code class="xref py py-class docutils literal notranslate"><span class="pre">MyImplementation</span></code></a>.</p>""",
    """
<dl class="py interface">
<dt id="sphinxcontrib.zopeext.example.IMyInterface">
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMyInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.x">
<code class="sig-name descname">x</code><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.x" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.equals">
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>""",
    """
<dl class="py interface">
<dt id="sphinxcontrib.zopeext.example.IMySecondInterface">
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMySecondInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMySecondInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>A refinement of the previous interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt id="sphinxcontrib.zopeext.example.IMySecondInterface.x">
<code class="sig-name descname">x</code><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMySecondInterface.x" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt id="sphinxcontrib.zopeext.example.IMySecondInterface.y">
<code class="sig-name descname">y</code><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMySecondInterface.y" title="Permalink to this definition">¶</a></dt>
<dd><p>A new required attribute</p>
</dd></dl>

<dl class="py method">
<dt id="sphinxcontrib.zopeext.example.IMySecondInterface.equals">
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMySecondInterface.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>""",
    """
<dl class="py class">
<dt id="sphinxcontrib.zopeext.example.MyImplementation">
<em class="property">class </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">MyImplementation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em>, <em class="sig-param"><span class="n">y</span><span class="o">=</span><span class="default_value">3.0</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.MyImplementation" title="Permalink to this definition">¶</a></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
</dd></dl>""",
    """
<div class="section" id="testing">
<h1>Testing<a class="headerlink" href="#testing" title="Permalink to this headline">¶</a></h1>
<p>We now check various options.</p>
<ul>
<li><p>The following also contain private members like <cite>_a</cite>:</p>
<p>Examples using <code class="xref py py-mod docutils literal notranslate"><span class="pre">zope.interface</span></code>.</p>
<p>Here we define an interface <a class="reference internal" href="#sphinxcontrib.zopeext.example.IMyInterface" title="sphinxcontrib.zopeext.example.IMyInterface"><code class="xref py py-class docutils literal notranslate"><span class="pre">IMyInterface</span></code></a> and an
implementation <a class="reference internal" href="#sphinxcontrib.zopeext.example.MyImplementation" title="sphinxcontrib.zopeext.example.MyImplementation"><code class="xref py py-class docutils literal notranslate"><span class="pre">MyImplementation</span></code></a>.</p>
<dl class="py interface">
<dt>
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMyInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt>
<code class="sig-name descname">_a</code></dt>
<dd><p>A private required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt>
<code class="sig-name descname">x</code></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py interface">
<dt>
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMySecondInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A refinement of the previous interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt>
<code class="sig-name descname">_a</code></dt>
<dd><p>A private required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt>
<code class="sig-name descname">x</code></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt>
<code class="sig-name descname">y</code></dt>
<dd><p>A new required attribute</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>
""",
    """
<dl class="py class">
<dt>
<em class="property">class </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">MyImplementation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em>, <em class="sig-param"><span class="n">y</span><span class="o">=</span><span class="default_value">3.0</span></em><span class="sig-paren">)</span></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
</dd></dl>
""",
    """
<li><p>Here is an explicit example of <cite>autointerface</cite></p>
<dl class="py interface">
<dt>
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMyInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt>
<code class="sig-name descname">x</code></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>""",
    """
<dl class="py interface">
<dt>
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMySecondInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>Bases: <a class="reference internal" href="#sphinxcontrib.zopeext.example.IMyInterface" title="sphinxcontrib.zopeext.example.IMyInterface"><code class="xref py py-class docutils literal notranslate"><span class="pre">sphinxcontrib.zopeext.example.IMyInterface</span></code></a></p>
<p>A refinement of the previous interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py attribute">
<dt>
<code class="sig-name descname">x</code></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="py attribute">
<dt>
<code class="sig-name descname">y</code></dt>
<dd><p>A new required attribute</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>
""",
    """
<li><p>Now with explicit members.</p>
<dl class="py interface">
<dt>
<em class="property">interface </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">IMyInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="py method">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.__init__">
<code class="sig-name descname">__init__</code><span class="sig-paren">(</span><em class="sig-param"><span class="o">**</span><span class="n">kw</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.__init__" title="Permalink to this definition">¶</a></dt>
<dd><p>The constructor should set the attribute <cite>x</cite>.</p>
</dd></dl>

<dl class="py attribute">
<dt>
<code class="sig-name descname">_a</code></dt>
<dd><p>A private required attribute of the interface</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>""",
    """
<li><p>Now with explicit members.</p>
<dl class="py class">
<dt>
<em class="property">class </em><code class="sig-prename descclassname">sphinxcontrib.zopeext.example.</code><code class="sig-name descname">MyImplementation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em>, <em class="sig-param"><span class="n">y</span><span class="o">=</span><span class="default_value">3.0</span></em><span class="sig-paren">)</span></dt>
<dd><p>Example</p>
<div class="doctest highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">a</span> <span class="o">=</span> <span class="n">MyImplementation</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="mf">2.0</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">a</span><span class="o">.</span><span class="n">equals</span><span class="p">(</span><span class="mf">2.0</span><span class="p">)</span>
<span class="go">True</span>
</pre></div>
</div>
<dl class="py method">
<dt id="sphinxcontrib.zopeext.example.MyImplementation.__init__">
<code class="sig-name descname">__init__</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em>, <em class="sig-param"><span class="n">y</span><span class="o">=</span><span class="default_value">3.0</span></em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.MyImplementation.__init__" title="Permalink to this definition">¶</a></dt>
<dd><p>Initialize self.  See help(type(self)) for accurate signature.</p>
</dd></dl>

<dl class="py method">
<dt>
<code class="sig-name descname">equals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">x</span></em><span class="sig-paren">)</span></dt>
<dd></dd></dl>

</dd></dl>""",
]
