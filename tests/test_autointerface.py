# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute

from sphinx_testing import with_app


@with_app(buildername='html',
          srcdir='tests/examples',
          copy_srcdir_to_tmpdir=True)
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / 'index.html').read_text()

    for _E in _EXPECTED:
        assert _E.strip() in html


_EXPECTED = ["""
  <dl class="interface">
<dt id="sphinxcontrib.zopeext.example.IMyInterface">
<em class="property">interface </em><code class="descclassname">sphinxcontrib.zopeext.example.</code><code class="descname">IMyInterface</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="attribute">
<dt id="sphinxcontrib.zopeext.example.IMyInterface._a">
<code class="descname">_a</code><em class="property"> = &lt;zope.interface.interface.Attribute object&gt;</em><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface._a" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="method">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.equals">
<code class="descname">equals</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

<dl class="attribute">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.x">
<code class="descname">x</code><em class="property"> = &lt;zope.interface.interface.Attribute object&gt;</em><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.x" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

</dd></dl>""",
             """
<dl class="interface">
<dt>
<em class="property">interface </em><code class="descclassname">sphinxcontrib.zopeext.example.</code><code class="descname">IMyInterface</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span></dt>
<dd><p>This is an example of an interface.</p>
<p>The constructor should set the attribute <cite>x</cite>.</p>
<dl class="attribute">
<dt>
<code class="descname">x</code><em class="property"> = &lt;zope.interface.interface.Attribute object&gt;</em></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="method">
<dt>
<code class="descname">equals</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span></dt>
<dd><p>A required method of the interface.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The argument <cite>self</cite> is not specified as part of the interface and
should be omitted, even though it is required in the implementation.</p>
</div>
</dd></dl>

</dd></dl>
"""]
