# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute

from sphinx_testing import with_app


class IMyInterface(Interface):
    """Test Interface"""
    x = Attribute("An attribute named x")

    def f(x):
        """A method named f with one argument x"""


@with_app(buildername='html',
          srcdir='tests/examples',
          copy_srcdir_to_tmpdir=True)
def test_sphinx_build(app, status, warning):
    app.build()
    html = (app.outdir / 'index.html').read_text()

    assert _EXPECTED.strip() in html


_EXPECTED = """
<dl class="interface">
<dt id="sphinxcontrib.zopeext.example.IMyInterface">
<em class="property">interface </em><code class="descclassname">sphinxcontrib.zopeext.example.</code><code class="descname">IMyInterface</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>This is an example of an interface.</p>
<dl class="attribute">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.x">
<code class="descname">x</code><em class="property"> = &lt;zope.interface.interface.Attribute object&gt;</em><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.x" title="Permalink to this definition">¶</a></dt>
<dd><p>A required attribute of the interface</p>
</dd></dl>

<dl class="method">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.__init__">
<code class="descname">__init__</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.__init__" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="method">
<dt id="sphinxcontrib.zopeext.example.IMyInterface.equals">
<code class="descname">equals</code><span class="sig-paren">(</span><em>x</em><span class="sig-paren">)</span><a class="headerlink" href="#sphinxcontrib.zopeext.example.IMyInterface.equals" title="Permalink to this definition">¶</a></dt>
<dd><p>A required method of the interface.</p>
</dd></dl>

</dd></dl>
"""
