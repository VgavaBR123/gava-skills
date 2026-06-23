# Interface — ui.* (apps e widgets do Code Editor)

> 293 funções. Referência completa da API — leia só este arquivo quando precisar deste tópico.

## Índice

- [`ui.Button`](#ui-button)
- [`ui.Button.getDisabled`](#ui-button-getdisabled)
- [`ui.Button.getImageUrl`](#ui-button-getimageurl)
- [`ui.Button.getLabel`](#ui-button-getlabel)
- [`ui.Button.onClick`](#ui-button-onclick)
- [`ui.Button.setDisabled`](#ui-button-setdisabled)
- [`ui.Button.setImageUrl`](#ui-button-setimageurl)
- [`ui.Button.setLabel`](#ui-button-setlabel)
- [`ui.Button.style`](#ui-button-style)
- [`ui.Button.unlisten`](#ui-button-unlisten)
- [`ui.Chart`](#ui-chart)
- [`ui.Chart.array.values`](#ui-chart-array-values)
- [`ui.Chart.feature.byFeature`](#ui-chart-feature-byfeature)
- [`ui.Chart.feature.byProperty`](#ui-chart-feature-byproperty)
- [`ui.Chart.feature.groups`](#ui-chart-feature-groups)
- [`ui.Chart.feature.histogram`](#ui-chart-feature-histogram)
- [`ui.Chart.getChartType`](#ui-chart-getcharttype)
- [`ui.Chart.getDataTable`](#ui-chart-getdatatable)
- [`ui.Chart.getDownloadable`](#ui-chart-getdownloadable)
- [`ui.Chart.getOptions`](#ui-chart-getoptions)
- [`ui.Chart.getView`](#ui-chart-getview)
- [`ui.Chart.image.byClass`](#ui-chart-image-byclass)
- [`ui.Chart.image.byRegion`](#ui-chart-image-byregion)
- [`ui.Chart.image.doySeries`](#ui-chart-image-doyseries)
- [`ui.Chart.image.doySeriesByRegion`](#ui-chart-image-doyseriesbyregion)
- [`ui.Chart.image.doySeriesByYear`](#ui-chart-image-doyseriesbyyear)
- [`ui.Chart.image.histogram`](#ui-chart-image-histogram)
- [`ui.Chart.image.regions`](#ui-chart-image-regions)
- [`ui.Chart.image.series`](#ui-chart-image-series)
- [`ui.Chart.image.seriesByRegion`](#ui-chart-image-seriesbyregion)
- [`ui.Chart.onClick`](#ui-chart-onclick)
- [`ui.Chart.setChartType`](#ui-chart-setcharttype)
- [`ui.Chart.setDataTable`](#ui-chart-setdatatable)
- [`ui.Chart.setDownloadable`](#ui-chart-setdownloadable)
- [`ui.Chart.setOptions`](#ui-chart-setoptions)
- [`ui.Chart.setSeriesNames`](#ui-chart-setseriesnames)
- [`ui.Chart.setView`](#ui-chart-setview)
- [`ui.Chart.style`](#ui-chart-style)
- [`ui.Chart.unlisten`](#ui-chart-unlisten)
- [`ui.Checkbox`](#ui-checkbox)
- [`ui.Checkbox.getDisabled`](#ui-checkbox-getdisabled)
- [`ui.Checkbox.getLabel`](#ui-checkbox-getlabel)
- [`ui.Checkbox.getValue`](#ui-checkbox-getvalue)
- [`ui.Checkbox.onChange`](#ui-checkbox-onchange)
- [`ui.Checkbox.setDisabled`](#ui-checkbox-setdisabled)
- [`ui.Checkbox.setLabel`](#ui-checkbox-setlabel)
- [`ui.Checkbox.setValue`](#ui-checkbox-setvalue)
- [`ui.Checkbox.style`](#ui-checkbox-style)
- [`ui.Checkbox.unlisten`](#ui-checkbox-unlisten)
- [`ui.DateSlider`](#ui-dateslider)
- [`ui.DateSlider.getDisabled`](#ui-dateslider-getdisabled)
- [`ui.DateSlider.getEnd`](#ui-dateslider-getend)
- [`ui.DateSlider.getPeriod`](#ui-dateslider-getperiod)
- [`ui.DateSlider.getStart`](#ui-dateslider-getstart)
- [`ui.DateSlider.getValue`](#ui-dateslider-getvalue)
- [`ui.DateSlider.onChange`](#ui-dateslider-onchange)
- [`ui.DateSlider.setDisabled`](#ui-dateslider-setdisabled)
- [`ui.DateSlider.setEnd`](#ui-dateslider-setend)
- [`ui.DateSlider.setPeriod`](#ui-dateslider-setperiod)
- [`ui.DateSlider.setStart`](#ui-dateslider-setstart)
- [`ui.DateSlider.setValue`](#ui-dateslider-setvalue)
- [`ui.DateSlider.style`](#ui-dateslider-style)
- [`ui.DateSlider.unlisten`](#ui-dateslider-unlisten)
- [`ui.Label`](#ui-label)
- [`ui.Label.getImageUrl`](#ui-label-getimageurl)
- [`ui.Label.getUrl`](#ui-label-geturl)
- [`ui.Label.getValue`](#ui-label-getvalue)
- [`ui.Label.setImageUrl`](#ui-label-setimageurl)
- [`ui.Label.setUrl`](#ui-label-seturl)
- [`ui.Label.setValue`](#ui-label-setvalue)
- [`ui.Label.style`](#ui-label-style)
- [`ui.Map`](#ui-map)
- [`ui.Map.CloudStorageLayer`](#ui-map-cloudstoragelayer)
- [`ui.Map.CloudStorageLayer.getBucket`](#ui-map-cloudstoragelayer-getbucket)
- [`ui.Map.CloudStorageLayer.getMaxZoom`](#ui-map-cloudstoragelayer-getmaxzoom)
- [`ui.Map.CloudStorageLayer.getName`](#ui-map-cloudstoragelayer-getname)
- [`ui.Map.CloudStorageLayer.getOpacity`](#ui-map-cloudstoragelayer-getopacity)
- [`ui.Map.CloudStorageLayer.getPath`](#ui-map-cloudstoragelayer-getpath)
- [`ui.Map.CloudStorageLayer.getShown`](#ui-map-cloudstoragelayer-getshown)
- [`ui.Map.CloudStorageLayer.getSuffix`](#ui-map-cloudstoragelayer-getsuffix)
- [`ui.Map.CloudStorageLayer.setBucket`](#ui-map-cloudstoragelayer-setbucket)
- [`ui.Map.CloudStorageLayer.setMaxZoom`](#ui-map-cloudstoragelayer-setmaxzoom)
- [`ui.Map.CloudStorageLayer.setName`](#ui-map-cloudstoragelayer-setname)
- [`ui.Map.CloudStorageLayer.setOpacity`](#ui-map-cloudstoragelayer-setopacity)
- [`ui.Map.CloudStorageLayer.setPath`](#ui-map-cloudstoragelayer-setpath)
- [`ui.Map.CloudStorageLayer.setShown`](#ui-map-cloudstoragelayer-setshown)
- [`ui.Map.CloudStorageLayer.setSuffix`](#ui-map-cloudstoragelayer-setsuffix)
- [`ui.Map.DrawingTools`](#ui-map-drawingtools)
- [`ui.Map.DrawingTools.addLayer`](#ui-map-drawingtools-addlayer)
- [`ui.Map.DrawingTools.clear`](#ui-map-drawingtools-clear)
- [`ui.Map.DrawingTools.draw`](#ui-map-drawingtools-draw)
- [`ui.Map.DrawingTools.edit`](#ui-map-drawingtools-edit)
- [`ui.Map.DrawingTools.get`](#ui-map-drawingtools-get)
- [`ui.Map.DrawingTools.getDrawModes`](#ui-map-drawingtools-getdrawmodes)
- [`ui.Map.DrawingTools.getLinked`](#ui-map-drawingtools-getlinked)
- [`ui.Map.DrawingTools.getMap`](#ui-map-drawingtools-getmap)
- [`ui.Map.DrawingTools.getSelected`](#ui-map-drawingtools-getselected)
- [`ui.Map.DrawingTools.getShape`](#ui-map-drawingtools-getshape)
- [`ui.Map.DrawingTools.getShown`](#ui-map-drawingtools-getshown)
- [`ui.Map.DrawingTools.layers`](#ui-map-drawingtools-layers)
- [`ui.Map.DrawingTools.onDraw`](#ui-map-drawingtools-ondraw)
- [`ui.Map.DrawingTools.onEdit`](#ui-map-drawingtools-onedit)
- [`ui.Map.DrawingTools.onErase`](#ui-map-drawingtools-onerase)
- [`ui.Map.DrawingTools.onLayerAdd`](#ui-map-drawingtools-onlayeradd)
- [`ui.Map.DrawingTools.onLayerConfig`](#ui-map-drawingtools-onlayerconfig)
- [`ui.Map.DrawingTools.onLayerRemove`](#ui-map-drawingtools-onlayerremove)
- [`ui.Map.DrawingTools.onLayerSelect`](#ui-map-drawingtools-onlayerselect)
- [`ui.Map.DrawingTools.onSelect`](#ui-map-drawingtools-onselect)
- [`ui.Map.DrawingTools.onShapeChange`](#ui-map-drawingtools-onshapechange)
- [`ui.Map.DrawingTools.set`](#ui-map-drawingtools-set)
- [`ui.Map.DrawingTools.setDrawModes`](#ui-map-drawingtools-setdrawmodes)
- [`ui.Map.DrawingTools.setLinked`](#ui-map-drawingtools-setlinked)
- [`ui.Map.DrawingTools.setSelected`](#ui-map-drawingtools-setselected)
- [`ui.Map.DrawingTools.setShape`](#ui-map-drawingtools-setshape)
- [`ui.Map.DrawingTools.setShown`](#ui-map-drawingtools-setshown)
- [`ui.Map.DrawingTools.stop`](#ui-map-drawingtools-stop)
- [`ui.Map.DrawingTools.toFeatureCollection`](#ui-map-drawingtools-tofeaturecollection)
- [`ui.Map.DrawingTools.unlisten`](#ui-map-drawingtools-unlisten)
- [`ui.Map.FeatureViewLayer`](#ui-map-featureviewlayer)
- [`ui.Map.FeatureViewLayer.getAssetId`](#ui-map-featureviewlayer-getassetid)
- [`ui.Map.FeatureViewLayer.getName`](#ui-map-featureviewlayer-getname)
- [`ui.Map.FeatureViewLayer.getOpacity`](#ui-map-featureviewlayer-getopacity)
- [`ui.Map.FeatureViewLayer.getShown`](#ui-map-featureviewlayer-getshown)
- [`ui.Map.FeatureViewLayer.getVisParams`](#ui-map-featureviewlayer-getvisparams)
- [`ui.Map.FeatureViewLayer.setAssetId`](#ui-map-featureviewlayer-setassetid)
- [`ui.Map.FeatureViewLayer.setName`](#ui-map-featureviewlayer-setname)
- [`ui.Map.FeatureViewLayer.setOpacity`](#ui-map-featureviewlayer-setopacity)
- [`ui.Map.FeatureViewLayer.setShown`](#ui-map-featureviewlayer-setshown)
- [`ui.Map.FeatureViewLayer.setVisParams`](#ui-map-featureviewlayer-setvisparams)
- [`ui.Map.GeometryLayer`](#ui-map-geometrylayer)
- [`ui.Map.GeometryLayer.fromGeometry`](#ui-map-geometrylayer-fromgeometry)
- [`ui.Map.GeometryLayer.geometries`](#ui-map-geometrylayer-geometries)
- [`ui.Map.GeometryLayer.get`](#ui-map-geometrylayer-get)
- [`ui.Map.GeometryLayer.getColor`](#ui-map-geometrylayer-getcolor)
- [`ui.Map.GeometryLayer.getEeObject`](#ui-map-geometrylayer-geteeobject)
- [`ui.Map.GeometryLayer.getLocked`](#ui-map-geometrylayer-getlocked)
- [`ui.Map.GeometryLayer.getName`](#ui-map-geometrylayer-getname)
- [`ui.Map.GeometryLayer.getShown`](#ui-map-geometrylayer-getshown)
- [`ui.Map.GeometryLayer.openConfigurationDialog`](#ui-map-geometrylayer-openconfigurationdialog)
- [`ui.Map.GeometryLayer.set`](#ui-map-geometrylayer-set)
- [`ui.Map.GeometryLayer.setColor`](#ui-map-geometrylayer-setcolor)
- [`ui.Map.GeometryLayer.setLocked`](#ui-map-geometrylayer-setlocked)
- [`ui.Map.GeometryLayer.setName`](#ui-map-geometrylayer-setname)
- [`ui.Map.GeometryLayer.setShown`](#ui-map-geometrylayer-setshown)
- [`ui.Map.GeometryLayer.toGeometry`](#ui-map-geometrylayer-togeometry)
- [`ui.Map.Layer`](#ui-map-layer)
- [`ui.Map.Layer.getEeObject`](#ui-map-layer-geteeobject)
- [`ui.Map.Layer.getName`](#ui-map-layer-getname)
- [`ui.Map.Layer.getOpacity`](#ui-map-layer-getopacity)
- [`ui.Map.Layer.getShown`](#ui-map-layer-getshown)
- [`ui.Map.Layer.getVisParams`](#ui-map-layer-getvisparams)
- [`ui.Map.Layer.setEeObject`](#ui-map-layer-seteeobject)
- [`ui.Map.Layer.setName`](#ui-map-layer-setname)
- [`ui.Map.Layer.setOpacity`](#ui-map-layer-setopacity)
- [`ui.Map.Layer.setShown`](#ui-map-layer-setshown)
- [`ui.Map.Layer.setVisParams`](#ui-map-layer-setvisparams)
- [`ui.Map.Linker`](#ui-map-linker)
- [`ui.Map.Linker.add`](#ui-map-linker-add)
- [`ui.Map.Linker.forEach`](#ui-map-linker-foreach)
- [`ui.Map.Linker.get`](#ui-map-linker-get)
- [`ui.Map.Linker.getJsArray`](#ui-map-linker-getjsarray)
- [`ui.Map.Linker.insert`](#ui-map-linker-insert)
- [`ui.Map.Linker.length`](#ui-map-linker-length)
- [`ui.Map.Linker.remove`](#ui-map-linker-remove)
- [`ui.Map.Linker.reset`](#ui-map-linker-reset)
- [`ui.Map.Linker.set`](#ui-map-linker-set)
- [`ui.Map.add`](#ui-map-add)
- [`ui.Map.addLayer`](#ui-map-addlayer)
- [`ui.Map.centerObject`](#ui-map-centerobject)
- [`ui.Map.clear`](#ui-map-clear)
- [`ui.Map.drawingTools`](#ui-map-drawingtools)
- [`ui.Map.getBounds`](#ui-map-getbounds)
- [`ui.Map.getCenter`](#ui-map-getcenter)
- [`ui.Map.getScale`](#ui-map-getscale)
- [`ui.Map.getZoom`](#ui-map-getzoom)
- [`ui.Map.insert`](#ui-map-insert)
- [`ui.Map.layers`](#ui-map-layers)
- [`ui.Map.onChangeBounds`](#ui-map-onchangebounds)
- [`ui.Map.onChangeCenter`](#ui-map-onchangecenter)
- [`ui.Map.onChangeZoom`](#ui-map-onchangezoom)
- [`ui.Map.onClick`](#ui-map-onclick)
- [`ui.Map.onIdle`](#ui-map-onidle)
- [`ui.Map.onTileLoaded`](#ui-map-ontileloaded)
- [`ui.Map.remove`](#ui-map-remove)
- [`ui.Map.setCenter`](#ui-map-setcenter)
- [`ui.Map.setControlVisibility`](#ui-map-setcontrolvisibility)
- [`ui.Map.setGestureHandling`](#ui-map-setgesturehandling)
- [`ui.Map.setLocked`](#ui-map-setlocked)
- [`ui.Map.setOptions`](#ui-map-setoptions)
- [`ui.Map.setZoom`](#ui-map-setzoom)
- [`ui.Map.style`](#ui-map-style)
- [`ui.Map.unlisten`](#ui-map-unlisten)
- [`ui.Map.widgets`](#ui-map-widgets)
- [`ui.Panel`](#ui-panel)
- [`ui.Panel.Layout.absolute`](#ui-panel-layout-absolute)
- [`ui.Panel.Layout.flow`](#ui-panel-layout-flow)
- [`ui.Panel.add`](#ui-panel-add)
- [`ui.Panel.clear`](#ui-panel-clear)
- [`ui.Panel.getLayout`](#ui-panel-getlayout)
- [`ui.Panel.insert`](#ui-panel-insert)
- [`ui.Panel.remove`](#ui-panel-remove)
- [`ui.Panel.setLayout`](#ui-panel-setlayout)
- [`ui.Panel.style`](#ui-panel-style)
- [`ui.Panel.widgets`](#ui-panel-widgets)
- [`ui.Select`](#ui-select)
- [`ui.Select.getDisabled`](#ui-select-getdisabled)
- [`ui.Select.getPlaceholder`](#ui-select-getplaceholder)
- [`ui.Select.getValue`](#ui-select-getvalue)
- [`ui.Select.items`](#ui-select-items)
- [`ui.Select.onChange`](#ui-select-onchange)
- [`ui.Select.setDisabled`](#ui-select-setdisabled)
- [`ui.Select.setPlaceholder`](#ui-select-setplaceholder)
- [`ui.Select.setValue`](#ui-select-setvalue)
- [`ui.Select.style`](#ui-select-style)
- [`ui.Select.unlisten`](#ui-select-unlisten)
- [`ui.Slider`](#ui-slider)
- [`ui.Slider.getDisabled`](#ui-slider-getdisabled)
- [`ui.Slider.getMax`](#ui-slider-getmax)
- [`ui.Slider.getMin`](#ui-slider-getmin)
- [`ui.Slider.getStep`](#ui-slider-getstep)
- [`ui.Slider.getValue`](#ui-slider-getvalue)
- [`ui.Slider.onChange`](#ui-slider-onchange)
- [`ui.Slider.onSlide`](#ui-slider-onslide)
- [`ui.Slider.setDisabled`](#ui-slider-setdisabled)
- [`ui.Slider.setMax`](#ui-slider-setmax)
- [`ui.Slider.setMin`](#ui-slider-setmin)
- [`ui.Slider.setStep`](#ui-slider-setstep)
- [`ui.Slider.setValue`](#ui-slider-setvalue)
- [`ui.Slider.style`](#ui-slider-style)
- [`ui.Slider.unlisten`](#ui-slider-unlisten)
- [`ui.SplitPanel`](#ui-splitpanel)
- [`ui.SplitPanel.getFirstPanel`](#ui-splitpanel-getfirstpanel)
- [`ui.SplitPanel.getOrientation`](#ui-splitpanel-getorientation)
- [`ui.SplitPanel.getPanel`](#ui-splitpanel-getpanel)
- [`ui.SplitPanel.getSecondPanel`](#ui-splitpanel-getsecondpanel)
- [`ui.SplitPanel.getWipe`](#ui-splitpanel-getwipe)
- [`ui.SplitPanel.setFirstPanel`](#ui-splitpanel-setfirstpanel)
- [`ui.SplitPanel.setOrientation`](#ui-splitpanel-setorientation)
- [`ui.SplitPanel.setPanel`](#ui-splitpanel-setpanel)
- [`ui.SplitPanel.setSecondPanel`](#ui-splitpanel-setsecondpanel)
- [`ui.SplitPanel.setWipe`](#ui-splitpanel-setwipe)
- [`ui.SplitPanel.style`](#ui-splitpanel-style)
- [`ui.SplitPanel.unlisten`](#ui-splitpanel-unlisten)
- [`ui.Textbox`](#ui-textbox)
- [`ui.Textbox.getDisabled`](#ui-textbox-getdisabled)
- [`ui.Textbox.getPlaceholder`](#ui-textbox-getplaceholder)
- [`ui.Textbox.getValue`](#ui-textbox-getvalue)
- [`ui.Textbox.onChange`](#ui-textbox-onchange)
- [`ui.Textbox.setDisabled`](#ui-textbox-setdisabled)
- [`ui.Textbox.setPlaceholder`](#ui-textbox-setplaceholder)
- [`ui.Textbox.setValue`](#ui-textbox-setvalue)
- [`ui.Textbox.style`](#ui-textbox-style)
- [`ui.Textbox.unlisten`](#ui-textbox-unlisten)
- [`ui.Thumbnail`](#ui-thumbnail)
- [`ui.Thumbnail.getImage`](#ui-thumbnail-getimage)
- [`ui.Thumbnail.getParams`](#ui-thumbnail-getparams)
- [`ui.Thumbnail.onClick`](#ui-thumbnail-onclick)
- [`ui.Thumbnail.setImage`](#ui-thumbnail-setimage)
- [`ui.Thumbnail.setParams`](#ui-thumbnail-setparams)
- [`ui.Thumbnail.style`](#ui-thumbnail-style)
- [`ui.Thumbnail.unlisten`](#ui-thumbnail-unlisten)
- [`ui.data.ActiveDictionary`](#ui-data-activedictionary)
- [`ui.data.ActiveDictionary.get`](#ui-data-activedictionary-get)
- [`ui.data.ActiveDictionary.set`](#ui-data-activedictionary-set)
- [`ui.data.ActiveList`](#ui-data-activelist)
- [`ui.data.ActiveList.add`](#ui-data-activelist-add)
- [`ui.data.ActiveList.forEach`](#ui-data-activelist-foreach)
- [`ui.data.ActiveList.get`](#ui-data-activelist-get)
- [`ui.data.ActiveList.getJsArray`](#ui-data-activelist-getjsarray)
- [`ui.data.ActiveList.insert`](#ui-data-activelist-insert)
- [`ui.data.ActiveList.length`](#ui-data-activelist-length)
- [`ui.data.ActiveList.remove`](#ui-data-activelist-remove)
- [`ui.data.ActiveList.reset`](#ui-data-activelist-reset)
- [`ui.data.ActiveList.set`](#ui-data-activelist-set)
- [`ui.root.add`](#ui-root-add)
- [`ui.root.clear`](#ui-root-clear)
- [`ui.root.getLayout`](#ui-root-getlayout)
- [`ui.root.insert`](#ui-root-insert)
- [`ui.root.onResize`](#ui-root-onresize)
- [`ui.root.remove`](#ui-root-remove)
- [`ui.root.setKeyHandler`](#ui-root-setkeyhandler)
- [`ui.root.setLayout`](#ui-root-setlayout)
- [`ui.root.widgets`](#ui-root-widgets)
- [`ui.url.get`](#ui-url-get)
- [`ui.url.set`](#ui-url-set)
- [`ui.util.clear`](#ui-util-clear)
- [`ui.util.clearTimeout`](#ui-util-cleartimeout)
- [`ui.util.debounce`](#ui-util-debounce)
- [`ui.util.getCurrentPosition`](#ui-util-getcurrentposition)
- [`ui.util.rateLimit`](#ui-util-ratelimit)
- [`ui.util.setInterval`](#ui-util-setinterval)
- [`ui.util.setTimeout`](#ui-util-settimeout)
- [`ui.util.throttle`](#ui-util-throttle)

---

## ui.Button

A clickable button with a text label.

| Usage | Returns |
|---|---|
| `ui.Button(*label*, *onClick*, *disabled*, *style*, *imageUrl*)` | ui.Button |

| Argument | Type | Details |
|---|---|---|
| `label` | String, optional | The button's label. Defaults to an empty string. |
| `onClick` | Function, optional | A callback fired when the button is clicked. The callback is passed the button widget. |
| `disabled` | Boolean, optional | Whether the button is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. Defaults to an empty object. |
| `imageUrl` | String, optional | Optional image url. If provided, the button will be rendered as an image and the value text will be shown on mouse hover. Only data: urls and icons loaded from gstatic.com are allowed. |

## ui.Button.getDisabled

Returns whether the button is disabled.

| Usage | Returns |
|---|---|
| `Button.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |

## ui.Button.getImageUrl

Returns the url of the image if it exists.

| Usage | Returns |
|---|---|
| `Button.getImageUrl()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |

## ui.Button.getLabel

Returns the button's label.

| Usage | Returns |
|---|---|
| `Button.getLabel()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |

## ui.Button.onClick

Registers a callback that's fired when the button is clicked.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Button.onClick(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |
| `callback` | Function | The callback to fire when the button is clicked. The callback is passed the button widget. |

## ui.Button.setDisabled

Sets whether the button is disabled.

Returns this button.

| Usage | Returns |
|---|---|
| `Button.setDisabled(disabled)` | ui.Button |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |
| `disabled` | Boolean | Whether the button is disabled. |

## ui.Button.setImageUrl

Shows the button as image, which will render instead of the label text.

Returns this button.

| Usage | Returns |
|---|---|
| `Button.setImageUrl(imageUrl)` | ui.Button |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |
| `imageUrl` | String | The url of the image. |

## ui.Button.setLabel

Sets the button's label.

Returns this button.

| Usage | Returns |
|---|---|
| `Button.setLabel(label)` | ui.Button |

| Argument | Type | Details |
|---|---|---|
| this: `ui.button` | ui.Button | The ui.Button instance. |
| `label` | String | The button's label. |

## ui.Button.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Button.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Button.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Button.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Chart

A chart widget.

| Usage | Returns |
|---|---|
| `ui.Chart(*dataTable*, *chartType*, *options*, *view*, *downloadable*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `dataTable` | List\[List\[Object\]\]\|Object\|String, optional | A 2-D array of data or a Google Visualization DataTable literal. See: http://developers.google.com/chart/interactive/docs/reference#DataTable |
| `chartType` | String, optional | The chart type; for example, 'ScatterChart', 'LineChart', and 'ColumnChart'. For the complete list of charts, see: https://developers.google.com/chart/interactive/docs/gallery |
| `options` | Object, optional | An object defining chart style options such as: |---| | ` title ` (string) The title of the chart. | | ` colors ` (Array) An array of colors used to draw the chart. | Its format should follow the Google Visualization API's options: https://developers.google.com/chart/interactive/docs/customizing_charts |
| `view` | Object, optional | Sets a DataView initializer object, which acts as a filter over the underlying data. See: https://developers.google.com/chart/interactive/docs/reference#DataView |
| `downloadable` | Boolean, optional | Whether the chart can be downloaded as CSV, SVG, and PNG. Defaults to true. |

## ui.Chart.array.values

Generates a Chart from an array. Plots separate series for each 1-D vector along the given axis.

- X-axis = Array index along axis, optionally labeled by xLabels.

- Y-axis = Value.

- Series = Vector, described by indices of the non-axis array axes.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.array.values(array, axis, *xLabels*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `array` | Array\|List\[Object\] | Array to chart. |
| `axis` | Number | The axis along which to generate the 1-D vector series. |
| `xLabels` | Array\|List\[Object\], optional | Labels for ticks along the x-axis of the chart. |

## ui.Chart.feature.byFeature

Generates a Chart from a set of features. Plots the value of one or more properties for each feature:

- X-axis = Features labeled by xProperty (default: 'system:index').

- Y-axis = Values of yProperties (default: all properties).

- Series = Names of yProperties.

The values are ordered along the x-axis in the same order as the input features.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.feature.byFeature(features, *xProperty*, *yProperties*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `features` | Feature\|FeatureCollection\|List\[Feature\] | The features to include in the chart. |
| `xProperty` | String, optional | The property used as the value of each feature on the x-axis. Defaults to 'system:index'. |
| `yProperties` | List\[String\]\|String, optional | Property or properties used on the y-axis. If omitted, all properties of all features will be charted on the y-axis (except xProperty). |

## ui.Chart.feature.byProperty

Generates a Chart from a set of features. Plots property values of one or more features.

- X-axis = Property name, labeled by xProperties (default: all properties).

- Y-axis = Property value (must be numeric).

- Series = Features, labeled by seriesProperty (default: 'system:index').

All properties except seriesProperty are included on the x-axis by default.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.feature.byProperty(features, *xProperties*, *seriesProperty*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `features` | Feature\|FeatureCollection\|List\[Feature\] | The features to include in the chart. |
| `xProperties` | List\[String\]\|Object\|String, optional | One of (1) a property to be plotted on the x-axis; (2) a list of properties to be plotted on the x-axis; or (3) a (property, label) dictionary specifying labels for properties to be used as values on the x-axis. If omitted, all properties will be plotted on the x-axis, labeled with their names. |
| `seriesProperty` | String, optional | The name of the property used to label each feature in the legend. Defaults to 'system:index'. |

## ui.Chart.feature.groups

Generates a Chart from a set of features. Plots the value of a given property across groups of features. Features with the same value of groupProperty will be grouped and plotted as a single series.

- X-axis = xProperty values.

- Y-axis = yProperty values.

- Series = Feature groups, by seriesProperty.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.feature.groups(features, xProperty, yProperty, seriesProperty)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `features` | Feature\|FeatureCollection\|List\[Feature\] | The features to include in the chart. |
| `xProperty` | String | Property to be used as the label for each feature on the x-axis. |
| `yProperty` | String | Property to be plotted on the y-axis. |
| `seriesProperty` | String | Property used to determine feature groups. Features with the same value of groupProperty will be plotted as a single series on the chart. |

## ui.Chart.feature.histogram

Generates a Chart from a set of features. Computes and plots a histogram of the given property.

- X-axis = Histogram buckets (of property value).

- Y-axis = Frequency (i.e., the number of features whose value of property lands within the x-axis bucket bounds).

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.feature.histogram(features, property, *maxBuckets*, *minBucketWidth*, *maxRaw*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `features` | Feature\|FeatureCollection\|List\[Feature\] | The features to include in the chart. |
| `property` | String | The name of the property to generate the histogram for. |
| `maxBuckets` | Number, optional | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. Not used when the value of property is non-numeric. |
| `minBucketWidth` | Number, optional | The minimum histogram bucket width, or null to allow any power of 2. Not used when property is non-numeric. |
| `maxRaw` | Number, optional | The number of values to accumulate before building the initial histogram. Not used when property is non-numeric. |

## ui.Chart.getChartType

Returns this chart's type; for example, 'ScatterChart', 'LineChart', and 'ColumnChart'. For the complete list of charts, see: https://developers.google.com/chart/interactive/docs/gallery

| Usage | Returns |
|---|---|
| `Chart.getChartType()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |

## ui.Chart.getDataTable

Returns the DataTable containing data for this chart. See: http://developers.google.com/chart/interactive/docs/reference#DataTable

| Usage | Returns |
|---|---|
| `Chart.getDataTable()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |

## ui.Chart.getDownloadable

Returns whether the chart can be downloaded as CSV, SVG, and PNG.

| Usage | Returns |
|---|---|
| `Chart.getDownloadable()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |

## ui.Chart.getOptions

Returns this chart's options. See: https://developers.google.com/chart/interactive/docs/customizing_charts

| Usage | Returns |
|---|---|
| `Chart.getOptions()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |

## ui.Chart.getView

Returns this chart's DataView initializer object, which acts as a filter over the underlying data in the chart. See: https://developers.google.com/chart/interactive/docs/reference#DataView

| Usage | Returns |
|---|---|
| `Chart.getView()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |

## ui.Chart.image.byClass

Generates a Chart from an image. Plots derived band values in classified regions in an image.

- X-axis = Band name (all bands except the class band are charted).

- Y-axis = Band value.

- Series = Class label.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.byClass(image, classBand, *region*, *reducer*, *scale*, *classLabels*, *xLabels*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | Classified image to derive band values from. |
| `classBand` | Number\|String | The class label band in this image. |
| `region` | Feature\|FeatureCollection\|Geometry, optional | The region to reduce. If omitted, uses the entire image. |
| `reducer` | Reducer, optional | Reducer that generates the value(s) for the y-axis. Must return a single value per band. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the reducer in meters. |
| `classLabels` | List.\[String\]\|List\[String\]\|Object, optional | A dictionary of labels used to identify classes in the series legend. If omitted, classes will be labeled with the value of classBand. |
| `xLabels` | List\[Object\], optional | A list of labels used to label bands on the xAxis. Must have one fewer elements than the number of image bands. If omitted, bands will be labeled with their names. If the labels are numeric (e.g., wavelengths), x-axis will be continuous. |

## ui.Chart.image.byRegion

Generates a Chart from an image. Extracts and plots band values in one or more regions in the image, with each band in a separate series.

- X-axis = Region labeled by xProperty (default: 'system:index')

- Y-axis = Reducer output.

- Series = Band name.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.byRegion(image, *regions*, *reducer*, *scale*, *xProperty*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | Image to extract band values from. |
| `regions` | Feature\|FeatureCollection\|Geometry\|List\[Feature\]\|List\[Geometry\], optional | Regions to reduce. Defaults to the image's footprint. |
| `reducer` | Reducer, optional | Reducer that generates the value(s) for the y-axis. Must return a single value per band. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the reducer in meters. |
| `xProperty` | String, optional | Property to be used as the label for each Region on the x-axis. Defaults to 'system:index'. |

## ui.Chart.image.doySeries

Generates a Chart from an ImageCollection. Plots derived values of each band in a region for a each day of the year.

- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).

- Y-axis: Derived band value (reduced within the region and across years).

- Series: Band names.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.doySeries(imageCollection, *region*, *regionReducer*, *scale*, *yearReducer*, *startDay*, *endDay*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `imageCollection` | ImageCollection | The ImageCollection to chart. |
| `region` | Feature\|FeatureCollection\|Geometry, optional | The region to reduce. Defaults to the union of all geometries in the image collection. |
| `regionReducer` | Reducer, optional | Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the region reducer in meters. |
| `yearReducer` | Reducer, optional | Reducer for aggregating regionReducer outputs across years (for a given day). Must return a single value. Defaults to ee.Reducer.mean(). |
| `startDay` | Number, optional | Day of year to start the series. Must be between 1 and 366. |
| `endDay` | Number, optional | Day of year to end the series. Must be between startDay and 366. |

## ui.Chart.image.doySeriesByRegion

Generates a Chart from an ImageCollection. Plots the derived value of the given band in different regions at each day-of-year.

- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).

- Y-axis: Derived band value (reduced within the region and across years).

- Series: Regions.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.doySeriesByRegion(imageCollection, bandName, regions, *regionReducer*, *scale*, *yearReducer*, *seriesProperty*, *startDay*, *endDay*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `imageCollection` | ImageCollection | The ImageCollection to chart. |
| `bandName` | Number\|String | The name of the band to chart. |
| `regions` | Feature\|FeatureCollection\|Geometry\|List\[Feature\]\|List\[Geometry\] | The regions to reduce. |
| `regionReducer` | Reducer, optional | Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the region reducer in meters. |
| `yearReducer` | Reducer, optional | Reducer for aggregating band values across years (for a given day of year). Must return a single value. Defaults to ee.Reducer.mean(). |
| `seriesProperty` | String, optional | Property of features in opt_regions to be used for series labels. Defaults to 'system:index'. |
| `startDay` | Number, optional | Day of year to start the series. Must be between 1 and 366. |
| `endDay` | Number, optional | Day of year to end the series. Must be between startDay and 366. |

## ui.Chart.image.doySeriesByYear

Generates a Chart from an ImageCollection. Plots the derived value of the given band in a region for each day-of-year across different years.

- X-axis: Day of year (startDay to endDay, defaults to 1 to 366).

- Y-axis: Derived band value (reduced within the region).

- Series: Years.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.doySeriesByYear(imageCollection, bandName, *region*, *regionReducer*, *scale*, *sameDayReducer*, *startDay*, *endDay*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `imageCollection` | ImageCollection | The ImageCollection to chart. |
| `bandName` | Number\|String | The name of the band to chart. |
| `region` | Feature\|FeatureCollection\|Geometry, optional | The region to reduce. Defaults to the union of all geometries in the image collection. |
| `regionReducer` | Reducer, optional | Reducer for aggregating band values within the region. Must return a single value. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the region reducer in meters. |
| `sameDayReducer` | Reducer, optional | Reducer for aggregating band values across images with the same (DoY, year) pair. Must return a single value. Defaults to ee.Reducer.mean(). |
| `startDay` | Number, optional | Day of year to start the series. Must be between 1 and 366. |
| `endDay` | Number, optional | Day of year to end the series. Must be between startDay and 366. |

## ui.Chart.image.histogram

Generates a Chart from an image. Computes and plots histograms of the values of the bands in the specified region of the image.

- X-axis: Histogram buckets (of band value).

- Y-axis: Frequency (number of pixels with a band value in the bucket).

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.histogram(image, *region*, *scale*, *maxBuckets*, *minBucketWidth*, *maxRaw*, *maxPixels*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | The image to generate a histogram from. |
| `region` | Feature\|FeatureCollection\|Geometry, optional | The region to reduce. If omitted, uses the entire image. |
| `scale` | Number, optional | The pixel scale used when applying the histogram reducer, in meters. |
| `maxBuckets` | Number, optional | The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2. |
| `minBucketWidth` | Number, optional | The minimum histogram bucket width, or null to allow any power of 2. |
| `maxRaw` | Number, optional | The number of values to accumulate before building the initial histogram. |
| `maxPixels` | Number, optional | If specified, overrides the maximum number of pixels allowed in the histogram reduction. Defaults to 1e6. |

## ui.Chart.image.regions

Generates a Chart from an image. Extracts and plots the value of each band in one or more regions.

- X-axis = Band labeled by xProperty (default: band name).

- Y-axis = Reducer output.

- Series = Region labeled by seriesProperty (default: 'system:index').

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.regions(image, *regions*, *reducer*, *scale*, *seriesProperty*, *xLabels*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `image` | Image | Image to extract band values from. |
| `regions` | Feature\|FeatureCollection\|Geometry\|List\[Feature\]\|List\[Geometry\], optional | Regions to reduce. Defaults to the image's footprint. |
| `reducer` | Reducer, optional | Reducer that generates the value(s) for the y-axis. Must return a single value per band. |
| `scale` | Number, optional | The pixel scale in meters. |
| `seriesProperty` | String, optional | Property to be used as the label for each region in the legend. Defaults to 'system:index'. |
| `xLabels` | List\[Object\], optional | A list of labels used for bands on the x-axis. Must have the same number of elements as the image bands. If omitted, bands will be labeled with their names. If the labels are numeric (e.g., wavelengths), x-axis will be continuous. |

## ui.Chart.image.series

Generates a Chart from an ImageCollection. Plots derived values of each band in a region across images. Usually a time series.

- X-axis: Image, labeled by xProperty value.

- Y-axis: Band value.

- Series: Band names.

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.series(imageCollection, region, *reducer*, *scale*, *xProperty*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `imageCollection` | ImageCollection | An ImageCollection with data to be included in the chart. |
| `region` | Feature\|FeatureCollection\|Geometry | The region to reduce. |
| `reducer` | Reducer, optional | Reducer that generates the values for the y-axis. Must return a single value. Defaults to ee.Reducer.mean(). |
| `scale` | Number, optional | Scale to use with the reducer in meters. |
| `xProperty` | String, optional | Property to be used as the label for each image on the x-axis. Defaults to 'system:time_start'. |

## ui.Chart.image.seriesByRegion

Generates a Chart from an image collection. Extracts and plots the value of the specified band in each region for each image in the collection. Usually a time series.

- X-axis = Image labeled by xProperty (default: 'system:time_start').

- Y-axis = Reducer output.

- Series = Region labeled by seriesProperty (default: 'system:index').

Returns a chart.

| Usage | Returns |
|---|---|
| `ui.Chart.image.seriesByRegion(imageCollection, regions, reducer, *band*, *scale*, *xProperty*, *seriesProperty*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| `imageCollection` | ImageCollection | An ImageCollection with data to be included in the chart. |
| `regions` | Feature\|FeatureCollection\|Geometry\|List\[Feature\]\|List\[Geometry\] | The regions to reduce. |
| `reducer` | Reducer | Reducer that generates the value for the y-axis. Must return a single value. |
| `band` | Number\|String, optional | The band name to reduce using the reducer. Defaults to the first band. |
| `scale` | Number, optional | Scale to use with the reducer in meters. |
| `xProperty` | String, optional | Property to be used as the label for each image on the x-axis. Defaults to 'system:time_start'. |
| `seriesProperty` | String, optional | Property of features in opt_regions to be used for series labels. Defaults to 'system:index'. |

## ui.Chart.onClick

Registers a callback that's fired when the chart is clicked.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Chart.onClick(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `callback` | Function | The callback to fire when the chart is clicked. The callback is passed three arguments: the x-value, the y-value, and the series name. Time values are represented in UTC epoch milliseconds, like "system:time_start" values on assets. If the user clicks on a legend entry to select an entire series, the x- and y-values are null. If the user clicks an already-selected point, all arguments are null, indicating the selection was cleared. |

## ui.Chart.setChartType

Sets the chartType of this chart.

Returns this chart.

| Usage | Returns |
|---|---|
| `Chart.setChartType(chartType)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `chartType` | String | The chart type; for example, 'ScatterChart', 'LineChart', and 'ColumnChart'. For the complete list of charts, see: https://developers.google.com/chart/interactive/docs/gallery |

## ui.Chart.setDataTable

Sets the DataTable containing data for this chart.

Returns this chart.

| Usage | Returns |
|---|---|
| `Chart.setDataTable(dataTable)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `dataTable` | List\[List\[Object\]\]\|Object\|String | A 2-D array of data to chart or a Google Visualization DataTable literal. See: http://developers.google.com/chart/interactive/docs/reference#DataTable |

## ui.Chart.setDownloadable

Sets a view for this chart.

Returns this chart.

| Usage | Returns |
|---|---|
| `Chart.setDownloadable(Whether)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `Whether` | Boolean | the chart can be downloaded as CSV, SVG, and PNG. |

## ui.Chart.setOptions

Sets options used to style this chart.

Returns this chart.

| Usage | Returns |
|---|---|
| `Chart.setOptions(options)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `options` | Object | An object defining chart style options such as: |---| | ` title ` (string) The title of the chart. | | ` colors ` (Array) An array of colors used to draw the chart. | Its format should follow the Google Visualization API's options: https://developers.google.com/chart/interactive/docs/customizing_charts |

## ui.Chart.setSeriesNames

Returns a copy of this chart with updated series names.

| Usage | Returns |
|---|---|
| `Chart.setSeriesNames(seriesNames, *seriesIndex*)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `seriesNames` | Dictionary\|Dictionary\[String\]\|List\|List\[String\]\|String | New series names. If it's a string, the name of the series at seriesIndex is set to seriesNames. If it's a list, the value at index i in the list is used as a label for series number i. If it's a dictionary or an object, it's treated as a map from existing series names to new series names. In the last two cases, seriesIndex is ignored. |
| `seriesIndex` | Number, optional | The index of the series to rename. Ignored if seriesNames is a list or dictionary. Series are 0-indexed. |

## ui.Chart.setView

Sets a view for this chart.

Returns this chart.

| Usage | Returns |
|---|---|
| `Chart.setView(view)` | ui.Chart |

| Argument | Type | Details |
|---|---|---|
| this: `ui.chart` | ui.Chart | The ui.Chart instance. |
| `view` | Object | A DataView initializer object, which acts as a filter over the underlying data in the chart. See: https://developers.google.com/chart/interactive/docs/reference#DataView |

## ui.Chart.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Chart.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Chart.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Chart.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Checkbox

A checkbox with a label.

| Usage | Returns |
|---|---|
| `ui.Checkbox(*label*, *value*, *onChange*, *disabled*, *style*)` | ui.Checkbox |

| Argument | Type | Details |
|---|---|---|
| `label` | String, optional | The checkbox's label. Defaults to an empty string. |
| `value` | Boolean, optional | Whether the checkbox is checked. A null value indicates that the checkbox is in an indeterminate state. Defaults to false. |
| `onChange` | Function, optional | A callback to fire when the value of the checkbox changes. The callback is passed a boolean indicating whether the checkbox is now checked and the checkbox widget. |
| `disabled` | Boolean, optional | Whether the checkbox is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |

## ui.Checkbox.getDisabled

Returns whether the checkbox is disabled.

| Usage | Returns |
|---|---|
| `Checkbox.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |

## ui.Checkbox.getLabel

Returns the checkbox's label.

| Usage | Returns |
|---|---|
| `Checkbox.getLabel()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |

## ui.Checkbox.getValue

Returns whether the checkbox is checked. A null value indicates the checkbox is in an indeterminate state.

| Usage | Returns |
|---|---|
| `Checkbox.getValue()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |

## ui.Checkbox.onChange

Registers a callback that's fired when the value of the checkbox changes.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Checkbox.onChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |
| `callback` | Function | The callback to fire when the value of the checkbox changes. The callback is passed a boolean indicating whether the checkbox is now checked and the checkbox widget. |

## ui.Checkbox.setDisabled

Sets whether the checkbox is disabled.

Returns this checkbox.

| Usage | Returns |
|---|---|
| `Checkbox.setDisabled(disabled)` | ui.Checkbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |
| `disabled` | Boolean | Whether the checkbox is disabled. |

## ui.Checkbox.setLabel

Sets the checkbox's label.

Returns this checkbox.

| Usage | Returns |
|---|---|
| `Checkbox.setLabel(value)` | ui.Checkbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |
| `value` | String | The new label for the checkbox. |

## ui.Checkbox.setValue

Sets whether the checkbox is checked.

Returns this checkbox.

| Usage | Returns |
|---|---|
| `Checkbox.setValue(value, *trigger*)` | ui.Checkbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.checkbox` | ui.Checkbox | The ui.Checkbox instance. |
| `value` | Boolean | Whether the checkbox is checked. A null value indicates the checkbox is in an indeterminate state. |
| `trigger` | Boolean, optional | Whether to trigger onChange callbacks when the checked property changes. Defaults to true. |

## ui.Checkbox.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Checkbox.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Checkbox.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Checkbox.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.DateSlider

A draggable target that ranges linearly between two dates. The date slider can be configured to display dates of various interval sizes, including day, 8-day, and year. The value of the slider is displayed as a label alongside it.

| Usage | Returns |
|---|---|
| `ui.DateSlider(*start*, *end*, *value*, *period*, *onChange*, *disabled*, *style*)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| `start` | Date\|Number\|String, optional | The start date, as a UTC timestamp, date string, or ee.Date. Defaults to one week ago. |
| `end` | Date\|Number\|String, optional | The end date, as a UTC timestamp, date string, or ee.Date. Defaults to today. |
| `value` | Date\|Number\|String, optional | The initial value. The value is an array consisting of the start and end date for the selected date range, but for convenience, it can be set by specifying the start date alone. Defaults to yesterday. |
| `period` | Number, optional | The interval size for values on the slider in days. Defaults to one. |
| `onChange` | Function, optional | A callback to fire when the slider's state changes. The callback is passed an ee.DateRange representing the slider's current value and the slider widget. |
| `disabled` | Boolean, optional | Whether the slider is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. Defaults to an empty object. |

## ui.DateSlider.getDisabled

Returns whether the slider is disabled.

| Usage | Returns |
|---|---|
| `DateSlider.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |

## ui.DateSlider.getEnd

Returns the slider's end date as a UTC timestamp.

| Usage | Returns |
|---|---|
| `DateSlider.getEnd()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |

## ui.DateSlider.getPeriod

Returns the slider's period interval.

| Usage | Returns |
|---|---|
| `DateSlider.getPeriod()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |

## ui.DateSlider.getStart

Returns the slider's start date as a UTC timestamp.

| Usage | Returns |
|---|---|
| `DateSlider.getStart()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |

## ui.DateSlider.getValue

Returns the slider's current value, and array with the start and end datetimes as epoch UTC timestamps.

| Usage | Returns |
|---|---|
| `DateSlider.getValue()` | List\[Number\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |

## ui.DateSlider.onChange

Registers a callback that's fired when the slider's value changes.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DateSlider.onChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `callback` | Function | The callback to fire when the slider's state changes. The callback is passed an ee.DateRange representing the slider's current value and the slider widget. |

## ui.DateSlider.setDisabled

Sets whether the slider is disabled.

Returns this slider.

| Usage | Returns |
|---|---|
| `DateSlider.setDisabled(disabled)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `disabled` | Boolean | Whether the slider is disabled. |

## ui.DateSlider.setEnd

Sets the end date of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `DateSlider.setEnd(value)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `value` | Number\|String | The slider's end date. |

## ui.DateSlider.setPeriod

Sets the period interval of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `DateSlider.setPeriod(value)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `value` | Number | The slider's period interval. |

## ui.DateSlider.setStart

Sets the start date of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `DateSlider.setStart(start)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `start` | Number\|String | The start date. Defaults to one week ago. |

## ui.DateSlider.setValue

Set the value of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `DateSlider.setValue(value, *trigger*)` | ui.DateSlider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.dateslider` | ui.DateSlider | The ui.DateSlider instance. |
| `value` | Number\|String | The value to set on the slider. |
| `trigger` | Boolean, optional | Whether to trigger onChange callbacks when the value property changes. Defaults to true. |

## ui.DateSlider.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `DateSlider.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.DateSlider.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `DateSlider.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Label

A text label.

| Usage | Returns |
|---|---|
| `ui.Label(*value*, *style*, *targetUrl*, *imageUrl*)` | ui.Label |

| Argument | Type | Details |
|---|---|---|
| `value` | String, optional | The text to display. Defaults to an empty string. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |
| `targetUrl` | String, optional | The url to link to. Defaults to an empty string. |
| `imageUrl` | String, optional | Optional image url. If provided, the label will be rendered as an image and the value text will be shown on mouse hover. Only data: urls and icons loaded from gstatic.com are allowed. |

## ui.Label.getImageUrl

Returns the url of the image if it exists.

| Usage | Returns |
|---|---|
| `Label.getImageUrl()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |

## ui.Label.getUrl

Returns the url of the label if it exists.

| Usage | Returns |
|---|---|
| `Label.getUrl()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |

## ui.Label.getValue

Returns the value of the label.

| Usage | Returns |
|---|---|
| `Label.getValue()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |

## ui.Label.setImageUrl

Sets the label to an image, which will render instead of the value text.

Returns this label.

| Usage | Returns |
|---|---|
| `Label.setImageUrl(imageUrl)` | ui.Label |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |
| `imageUrl` | String | The url of the image. |

## ui.Label.setUrl

Sets the url of the label, which will cause it to render as a link.

Returns this label.

| Usage | Returns |
|---|---|
| `Label.setUrl(targetUrl)` | ui.Label |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |
| `targetUrl` | String | The url of the hyperlink. |

## ui.Label.setValue

Sets the value of the label.

Returns this label.

| Usage | Returns |
|---|---|
| `Label.setValue(value)` | ui.Label |

| Argument | Type | Details |
|---|---|---|
| this: `ui.label` | ui.Label | The ui.Label instance. |
| `value` | String | The value of the label. |

## ui.Label.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Label.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Map

A Google map.

| Usage | Returns |
|---|---|
| `ui.Map(*center*, *onClick*, *style*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| `center` | Object, optional | An object containing the latitude ('lat'), longitude ('lon') and optionally the zoom level ('zoom') for the map. |
| `onClick` | Function, optional | A callback fired when the map is clicked. The callback is passed an object containing the coordinates of the clicked point on the map (with keys lon and lat) and the map widget itself. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this map. See style() documentation. |

## ui.Map.CloudStorageLayer

A layer generated from Cloud Storage tiles for display on a ui.Map.

| Usage | Returns |
|---|---|
| `ui.Map.CloudStorageLayer(bucket, path, maxZoom, *suffix*, *name*, *shown*, *opacity*)` | ui.Map.CloudStorageLayer |

| Argument | Type | Details |
|---|---|---|
| `bucket` | String | The bucket that contains the tiles. |
| `path` | String | The path to this layer's tiles, relative to the bucket. A trailing "/" is optional. |
| `maxZoom` | Number | The maximum zoom level for which there are tiles. |
| `suffix` | String, optional | The tile source file suffix, if any. |
| `name` | String, optional | The name of the layer. |
| `shown` | Boolean, optional | Whether the layer is initially shown. Defaults to true. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. Defaults to 1. |

## ui.Map.CloudStorageLayer.getBucket

Returns the name of this layer's bucket.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getBucket()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |

## ui.Map.CloudStorageLayer.getMaxZoom

Returns the maximum zoom level of this layer's tileset.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getMaxZoom()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |

## ui.Map.CloudStorageLayer.getName

Returns the name of the layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getName()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.CloudStorageLayer.getOpacity

Returns the layer's opacity represented as a number between 0 and 1.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getOpacity()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.CloudStorageLayer.getPath

Returns the path within the bucket to the tiles.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getPath()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |

## ui.Map.CloudStorageLayer.getShown

Returns whether the layer is shown.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getShown()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.CloudStorageLayer.getSuffix

Returns the suffix for this layer's tile files.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.getSuffix()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |

## ui.Map.CloudStorageLayer.setBucket

Sets the bucket for this layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setBucket(bucket)` | ui.Map.CloudStorageLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |
| `bucket` | String | The name of the Cloud Storage bucket with this layer's tiles. |

## ui.Map.CloudStorageLayer.setMaxZoom

Sets the maximum zoom level for tiles. When the user zooms in beyond this level, the parent tile at this level will be fetched and zoomed on the client.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setMaxZoom(maxZoom)` | ui.Map.CloudStorageLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |
| `maxZoom` | Number | The maximum zoom level with tiles. |

## ui.Map.CloudStorageLayer.setName

Sets the name of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setName(*name*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `name` | String, optional | The name of the layer. |

## ui.Map.CloudStorageLayer.setOpacity

Sets the opacity of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setOpacity(*opacity*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. |

## ui.Map.CloudStorageLayer.setPath

Sets the location of the folder from which the layer will retrieve its tiles.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setPath(path)` | ui.Map.CloudStorageLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |
| `path` | String | The path to this layer's tiles, relative to the bucket. |

## ui.Map.CloudStorageLayer.setShown

Sets the visibility of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setShown(*shown*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `shown` | Boolean, optional | Whether the layer is shown. |

## ui.Map.CloudStorageLayer.setSuffix

Sets the CloudStorageLayer's file suffix.

Returns this map layer.

| Usage | Returns |
|---|---|
| `CloudStorageLayer.setSuffix(suffix)` | ui.Map.CloudStorageLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.cloudstoragelayer` | ui.Map.CloudStorageLayer | The ui.Map.CloudStorageLayer instance. |
| `suffix` | String | The suffix for the tile files, for example ".png". |

## ui.Map.DrawingTools

A set of tools for drawing on a map.

| Usage | Returns |
|---|---|
| `ui.Map.DrawingTools(*layers*, *shape*, *selected*, *shown*, *linked*)` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| `layers` | List\[ui.Map.GeometryLayer\], optional | An array of geometry layers with which to initialize the drawing tools. |
| `shape` | String, optional | The shape to draw. One of the following: point, line, polygon, or rectangle. Defaults to polygon. |
| `selected` | ui.Map.GeometryLayer, optional | The selected geometry layer. Defaults to null. |
| `shown` | Boolean, optional | When false, hides the drawing tools or, when true, shows the shape selector and allows the list panel's visibility to be determined by the presence of geometry layers in the list. Defaults to true. |
| `linked` | Boolean, optional | Whether the drawing tools are linked to the geometries in the imports pane. When false, the tools do not display imported geometries. Defaults to false. |

## ui.Map.DrawingTools.addLayer

Adds a given list of ee.Geometry objects to the drawing tools as a geometry layer.

Returns the new geometry layer.

| Usage | Returns |
|---|---|
| `DrawingTools.addLayer(geometries, *name*, *color*, *shown*, *locked*)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `geometries` | List\[Geometry\] | The geometries with which to initialize the layer. |
| `name` | String, optional | The name of the layer. |
| `color` | String, optional | The CSS color of shapes in the layer, for instance "white" or "#FFFFFF". |
| `shown` | Boolean, optional | Whether to show the shapes in the layer. Defaults to true. |
| `locked` | Boolean, optional | Whether to lock shape editing in the layer. Defaults to false. |

## ui.Map.DrawingTools.clear

Clears the drawing tools.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.clear()` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.draw

Enters drawing mode, in which a click on the map will begin drawing the selected shape.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.draw()` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.edit

Starts editing the selected layer.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.edit()` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.get

Returns either a clone of this object or, if a key is provided, the value of the property with the passed-in key. Look at the constructor's parameters to see which properties are available.

| Usage | Returns |
|---|---|
| `DrawingTools.get(*key*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `key` | String, optional | The key of the property to retrieve. |

## ui.Map.DrawingTools.getDrawModes

Gets the available draw modes on the drawing tool. The available draw mode shapes are: point, line, polygon, and rectangle.

Returns the list of enabled draw modes.

| Usage | Returns |
|---|---|
| `DrawingTools.getDrawModes()` | List\[String\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.getLinked

Returns whether the drawing tools' geometries are linked to those in the imports panel.

| Usage | Returns |
|---|---|
| `DrawingTools.getLinked()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.getMap

Returns the map for these drawing tools or null if the drawing tools have not been added to a map.

| Usage | Returns |
|---|---|
| `DrawingTools.getMap()` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.getSelected

Returns the selected layer.

| Usage | Returns |
|---|---|
| `DrawingTools.getSelected()` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.getShape

Returns the shape drawn when in drawing mode.

| Usage | Returns |
|---|---|
| `DrawingTools.getShape()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.getShown

Returns whether the drawing tools are shown.

| Usage | Returns |
|---|---|
| `DrawingTools.getShown()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.layers

Returns the list of geometry layers in the drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.layers()` | ui.data.ActiveList\[ui.Map.GeometryLayer\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.onDraw

Registers a callback that's fired when a shape is drawn.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onDraw(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a shape is drawn. The callback is passed three parameters: the added ee.Geometry, the GeometryLayer to which the geometry was added, and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onEdit

Registers a callback that's fired when a shape is edited.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onEdit(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a shape is edited. The callback is passed three parameters: the edited ee.Geometry, the GeometryLayer to which the edited geometry belongs, and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onErase

Registers a callback that's fired when a shape is erased.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onErase(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a shape is erased. The callback is passed three parameters: the removed ee.Geometry, the GeometryLayer from which the geometry was removed, and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onLayerAdd

Registers a callback that's fired when a layer is added.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onLayerAdd(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a layer is added. The callback is passed two parameters: the added GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onLayerConfig

Registers a callback that's fired after a layer's name or color is changed.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onLayerConfig(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire after a layer is configured. The callback is passed two parameters: the configured GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onLayerRemove

Registers a callback that's fired when a layer is removed.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onLayerRemove(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a layer is removed. The callback is passed two parameters: the removed GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onLayerSelect

Registers a callback that's fired when a layer is selected.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onLayerSelect(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a shape is selected. The callback is passed two parameters: the selected GeometryLayer (or null for deselect) and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onSelect

Registers a callback that's fired when a shape is selected.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onSelect(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when a shape is selected. The callback is passed three parameters: the selected ee.Geometry, the GeometryLayer to which the selected geometry belongs, and the ui.Map.DrawingTools widget that the event listener is bound to. |

## ui.Map.DrawingTools.onShapeChange

Registers a callback that's fired when a drawing mode shape is changed.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `DrawingTools.onShapeChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `callback` | Function | The callback to fire when the shape is changed. The callback is passed two parameters: the drawing mode shape as a string (or null for cancel) and the ui.Map.DrawingTools widget that the event listener is bound to. The shape values are: - point - line - polygon - rectangle - null |

## ui.Map.DrawingTools.set

Sets the value of a given property. Throws an error if the key provided is not supported by the object. Look at the constructor's parameters to see which properties can be set.

Returns this ui.data.ActiveDictionary.

| Usage | Returns |
|---|---|
| `DrawingTools.set(keyOrDict, *value*)` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `keyOrDict` | Object\|String | Either the key of the property to set or a dictionary of key/value pairs to set on the object. |
| `value` | Object, optional | The property's new value. This is required when the first argument is a key string. |

## ui.Map.DrawingTools.setDrawModes

Sets the available draw mode shapes on the drawing tool. The available draw mode shapes are: point, line, polygon, and rectangle.

| Usage | Returns |
|---|---|
| `DrawingTools.setDrawModes(*drawModes*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `drawModes` | List\[String\], optional | The list of draw modes to enable. Defaults to all supported ones. |

## ui.Map.DrawingTools.setLinked

Sets whether the drawing tools' geometries are linked to the imports panel or isolated to the map.

Returns these ui.Map.DrawingTools.

| Usage | Returns |
|---|---|
| `DrawingTools.setLinked(linked)` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `linked` | Boolean | Whether the geometries should be linked to the imports panel. When false, all geometries are local to the map instance. |

## ui.Map.DrawingTools.setSelected

Sets the selected layer.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.setSelected(*layer*)` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `layer` | ui.Map.GeometryLayer, optional | The layer to select or null to deselect all layers. |

## ui.Map.DrawingTools.setShape

Sets the draw mode shape and starts draw mode. The available draw mode shapes are: point, line, polygon, and rectangle.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.setShape(shape)` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `shape` | String | The shape to draw. |

## ui.Map.DrawingTools.setShown

Sets the visibility of the shape selector and geometry layer list.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.setShown(shown)` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `shown` | Boolean | Whether to show the drawing tools. |

## ui.Map.DrawingTools.stop

Closes the drawing tools, exiting interactive drawing or editing.

Returns this set of drawing tools.

| Usage | Returns |
|---|---|
| `DrawingTools.stop()` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |

## ui.Map.DrawingTools.toFeatureCollection

Returns a feature collection in which each geometry in the drawing tools is a feature.

| Usage | Returns |
|---|---|
| `DrawingTools.toFeatureCollection(indexProperty)` | FeatureCollection |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `indexProperty` | String | A property with this name will be assigned to every feature in the returned collection. The value of the property will be a number that corresponds to the index of the geometry layer to which the geometry belongs. |

## ui.Map.DrawingTools.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `DrawingTools.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Map.FeatureViewLayer

A layer generated from a FeatureView asset for display on a ui.Map.

| Usage | Returns |
|---|---|
| `ui.Map.FeatureViewLayer(assetId, *visParams*, *name*, *shown*, *opacity*)` | ui.Map.FeatureViewLayer |

| Argument | Type | Details |
|---|---|---|
| `assetId` | String | The asset ID for the FeatureView. |
| `visParams` | Object, optional | The visualization parameters for this layer. |
| `name` | String, optional | The name of the layer, which appears in the list of layers and when inspecting this layer. Defaults to the asset ID. |
| `shown` | Boolean, optional | Whether the layer is initially shown on the map. Defaults to true. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. Defaults to 1. |

## ui.Map.FeatureViewLayer.getAssetId

Returns the asset ID for the FeatureView asset backing this layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.getAssetId()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.featureviewlayer` | ui.Map.FeatureViewLayer | The ui.Map.FeatureViewLayer instance. |

## ui.Map.FeatureViewLayer.getName

Returns the name of the layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.getName()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.FeatureViewLayer.getOpacity

Returns the layer's opacity represented as a number between 0 and 1.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.getOpacity()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.FeatureViewLayer.getShown

Returns whether the layer is shown.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.getShown()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.FeatureViewLayer.getVisParams

Returns the visualization parameters for this layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.getVisParams()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.featureviewlayer` | ui.Map.FeatureViewLayer | The ui.Map.FeatureViewLayer instance. |

## ui.Map.FeatureViewLayer.setAssetId

Changes the asset being displayed on this layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.setAssetId(assetId)` | ui.Map.FeatureViewLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.featureviewlayer` | ui.Map.FeatureViewLayer | The ui.Map.FeatureViewLayer instance. |
| `assetId` | String | The asset ID for the FeatureView backing this layer. |

## ui.Map.FeatureViewLayer.setName

Sets the name of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.setName(*name*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `name` | String, optional | The name of the layer. |

## ui.Map.FeatureViewLayer.setOpacity

Sets the opacity of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.setOpacity(*opacity*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. |

## ui.Map.FeatureViewLayer.setShown

Sets the visibility of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.setShown(*shown*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `shown` | Boolean, optional | Whether the layer is shown. |

## ui.Map.FeatureViewLayer.setVisParams

Sets the visualization parameters for this layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `FeatureViewLayer.setVisParams(*visParams*)` | ui.Map.FeatureViewLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.featureviewlayer` | ui.Map.FeatureViewLayer | The ui.Map.FeatureViewLayer instance. |
| `visParams` | Object, optional | The visualization parameters for this layer. |

## ui.Map.GeometryLayer

A layer of ee.Geometries for display as shapes on a ui.Map.

| Usage | Returns |
|---|---|
| `ui.Map.GeometryLayer(*geometries*, *name*, *color*, *shown*, *locked*)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| `geometries` | List\[Geometry\], optional | The geometries with which to initialize the layer. |
| `name` | String, optional | The name of the layer. |
| `color` | String, optional | The CSS color of shapes in the layer, for instance "white" or "#FFFFFF". Defaults to "#000000" (black). |
| `shown` | Boolean, optional | Whether to show the shapes in the layer. Defaults to true. |
| `locked` | Boolean, optional | Whether to lock shape editing in the layer. Defaults to false. |

## ui.Map.GeometryLayer.fromGeometry

Resets the layer's geometries by parsing individual geometries from an ee.Geometry.

Returns this geometry layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.fromGeometry(geometry)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |
| `geometry` | Geometry | A geometry with which to reset the layer's geometries. |

## ui.Map.GeometryLayer.geometries

Returns the active list of geometries associated with the layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.geometries()` | ui.data.ActiveList\[Geometry\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.get

Returns either a clone of this object or, if a key is provided, the value of the property with the passed-in key. Look at the constructor's parameters to see which properties are available.

| Usage | Returns |
|---|---|
| `GeometryLayer.get(*key*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `key` | String, optional | The key of the property to retrieve. |

## ui.Map.GeometryLayer.getColor

Returns the color of the layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.getColor()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.getEeObject

Returns the EE object associated with the layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.getEeObject()` | Feature\|FeatureCollection\|Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.getLocked

Returns whether the shapes in the layer are shown.

| Usage | Returns |
|---|---|
| `GeometryLayer.getLocked()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.getName

Returns the name of the layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.getName()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.getShown

Returns whether the shapes in the layer are shown.

| Usage | Returns |
|---|---|
| `GeometryLayer.getShown()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.openConfigurationDialog

Opens a configuration dialog for the layer. Use onLayerConfig to register a callback for when the user makes changes using the dialog.

Returns the geometry layer to be updated by the dialog.

| Usage | Returns |
|---|---|
| `GeometryLayer.openConfigurationDialog()` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.GeometryLayer.set

Sets the value of a given property. Throws an error if the key provided is not supported by the object. Look at the constructor's parameters to see which properties can be set.

Returns this ui.data.ActiveDictionary.

| Usage | Returns |
|---|---|
| `GeometryLayer.set(keyOrDict, *value*)` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `keyOrDict` | Object\|String | Either the key of the property to set or a dictionary of key/value pairs to set on the object. |
| `value` | Object, optional | The property's new value. This is required when the first argument is a key string. |

## ui.Map.GeometryLayer.setColor

Sets the CSS color of shapes in the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.setColor(color)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |
| `color` | String | The color of the layer. |

## ui.Map.GeometryLayer.setLocked

Sets the locked state of the layer. A locked layer disallows adding, removing, or editing the geometries on the layer from the user interface.

Returns this map layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.setLocked(locked)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |
| `locked` | Boolean | Whether the layer is locked. |

## ui.Map.GeometryLayer.setName

Sets the name of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.setName(name)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |
| `name` | String | The name of the layer. |

## ui.Map.GeometryLayer.setShown

Sets the visibility of shapes in the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `GeometryLayer.setShown(shown)` | ui.Map.GeometryLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |
| `shown` | Boolean | Whether the layer is shown. |

## ui.Map.GeometryLayer.toGeometry

Returns the layer's geometries as a single ee.Geometry.

| Usage | Returns |
|---|---|
| `GeometryLayer.toGeometry()` | Geometry |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.geometrylayer` | ui.Map.GeometryLayer | The ui.Map.GeometryLayer instance. |

## ui.Map.Layer

A layer generated from an Earth Engine object for display on a ui.Map.

| Usage | Returns |
|---|---|
| `ui.Map.Layer(*eeObject*, *visParams*, *name*, *shown*, *opacity*)` | ui.Map.Layer |

| Argument | Type | Details |
|---|---|---|
| `eeObject` | Collection\|Feature\|Image, optional | The object to add to the map. Defaults to an empty ee.Image. |
| `visParams` | FeatureVisualizationParameters\|ImageVisualizationParameters, optional | The visualization parameters. See ee.data.getMapId() docs. |
| `name` | String, optional | The name of the layer. |
| `shown` | Boolean, optional | Whether the layer is initially shown. Defaults to true. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. Defaults to 1. |

## ui.Map.Layer.getEeObject

Returns the layer's ee.Object.

| Usage | Returns |
|---|---|
| `Layer.getEeObject()` | Collection\|Feature\|Image |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.layer` | ui.Map.Layer | The ui.Map.Layer instance. |

## ui.Map.Layer.getName

Returns the name of the layer.

| Usage | Returns |
|---|---|
| `Layer.getName()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.Layer.getOpacity

Returns the layer's opacity represented as a number between 0 and 1.

| Usage | Returns |
|---|---|
| `Layer.getOpacity()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.Layer.getShown

Returns whether the layer is shown.

| Usage | Returns |
|---|---|
| `Layer.getShown()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |

## ui.Map.Layer.getVisParams

Returns the layer's visualization parameters.

| Usage | Returns |
|---|---|
| `Layer.getVisParams()` | FeatureVisualizationParameters\|ImageVisualizationParameters |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.layer` | ui.Map.Layer | The ui.Map.Layer instance. |

## ui.Map.Layer.setEeObject

Sets the layer's ee.Object.

Returns this map layer.

| Usage | Returns |
|---|---|
| `Layer.setEeObject(*eeObject*)` | ui.Map.Layer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.layer` | ui.Map.Layer | The ui.Map.Layer instance. |
| `eeObject` | Collection\|Feature\|Image, optional | The object to add to the map. Defaults to an empty ee.Image. |

## ui.Map.Layer.setName

Sets the name of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `Layer.setName(*name*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `name` | String, optional | The name of the layer. |

## ui.Map.Layer.setOpacity

Sets the opacity of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `Layer.setOpacity(*opacity*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. |

## ui.Map.Layer.setShown

Sets the visibility of the layer.

Returns this map layer.

| Usage | Returns |
|---|---|
| `Layer.setShown(*shown*)` | ui.Map.AbstractLayer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.abstractlayer` | ui.Map.AbstractLayer | The ui.Map.AbstractLayer instance. |
| `shown` | Boolean, optional | Whether the layer is shown. |

## ui.Map.Layer.setVisParams

Sets the layer's visualization parameters.

Returns this map layer.

| Usage | Returns |
|---|---|
| `Layer.setVisParams(*visParams*)` | ui.Map.Layer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map.layer` | ui.Map.Layer | The ui.Map.Layer instance. |
| `visParams` | FeatureVisualizationParameters\|ImageVisualizationParameters, optional | The visualization parameters. See ee.data.getMapId() docs. |

## ui.Map.Linker

A utility for creating linked maps.

| Usage | Returns |
|---|---|
| `ui.Map.Linker(*maps*, *event*)` | ui.Map.Linker |

| Argument | Type | Details |
|---|---|---|
| `maps` | List\[Object\], optional | A list of maps to link. |
| `event` | String, optional | The event to link across the maps. Defaults to "change-bounds". Possible events comprise: - change-bounds - change-center - change-zoom |

## ui.Map.Linker.add

Appends an element to the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `Linker.add(el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `el` | Object | The element to add. |

## ui.Map.Linker.forEach

Iterates over each element, calling the provided callback. The callback is called for each element like: callback(element, index).

| Usage | Returns |
|---|---|
| `Linker.forEach(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `callback` | Function |   |

## ui.Map.Linker.get

Returns the element at the specified index.

| Usage | Returns |
|---|---|
| `Linker.get(index)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index of the element to return. |

## ui.Map.Linker.getJsArray

Returns the list as a JS array.

| Usage | Returns |
|---|---|
| `Linker.getJsArray()` | List\[Object\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |

## ui.Map.Linker.insert

Inserts an element at the specified index and shifts the rest of the list. If the specified index is greater than the length of the list, the element will be appended to the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `Linker.insert(index, el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index at which to insert the element. |
| `el` | Object | The element to insert. |

## ui.Map.Linker.length

Returns the number of elements in the list.

| Usage | Returns |
|---|---|
| `Linker.length()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |

## ui.Map.Linker.remove

Removes the specified element from the list.

Returns the removed element or null if the element was not present in the list.

| Usage | Returns |
|---|---|
| `Linker.remove(el)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `el` | Object | The element to remove. |

## ui.Map.Linker.reset

Replaces all elements in list with a new list or, if no list is provided, removes all elements from list.

Returns the elements in the list after the reset is applied.

| Usage | Returns |
|---|---|
| `Linker.reset(*list*)` | List\[Object\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `list` | List\[Object\], optional | A list of elements. |

## ui.Map.Linker.set

Sets an element at the specified index. If the index exceeds that of the list's last element, the element will be added to the end of the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `Linker.set(index, el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index to overwrite. |
| `el` | Object | The element to set. |

## ui.Map.add

Adds an item to the map. Can also be used to add widgets like ui.Label as well as some non-widget objects like ui.Map.Layer.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.add(item)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `item` | Object | The item to add. |

## ui.Map.addLayer

Adds a given EE object to the map as a layer.

Returns the new map layer.

| Usage | Returns |
|---|---|
| `Map.addLayer(eeObject, *visParams*, *name*, *shown*, *opacity*)` | ui.Map.Layer |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `eeObject` | Collection\|Feature\|Image\|MapId | The object to add to the map. |
| `visParams` | FeatureVisualizationParameters\|ImageVisualizationParameters, optional | The visualization parameters. For Images and ImageCollection, see ee.data.getMapId for valid parameters. For Features and FeatureCollections, the only supported key is "color", as a 6-character hex string in the RRGGBB format. |
| `name` | String, optional | The name of the layer. Defaults to "Layer N". |
| `shown` | Boolean, optional | A flag indicating whether the layer should be on by default. |
| `opacity` | Number, optional | The layer's opacity represented as a number between 0 and 1. Defaults to 1. |

## ui.Map.centerObject

Centers the map view on a given object.

> [!CAUTION]
> **Caution:** providing a large or complex collection as input can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.centerObject(object, *zoom*, *onComplete*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `object` | Element\|Geometry | An object to center on - a geometry, image or feature. |
| `zoom` | Number, optional | The zoom level, from 0 to 24. If unspecified, computed based on the object's bounding box. |
| `onComplete` | Function, optional | A callback which is triggered after the recentering completes successfully. Passing this parameter causes the \`centerObject\` operation to run asynchronously. |

## ui.Map.clear

Clears the map by removing all layers, listeners, and widgets and restoring the options to their defaults.

Returns the map.

| Usage | Returns |
|---|---|
| `Map.clear()` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.drawingTools

Returns the map's drawing tools, which can be used to create and edit shapes on the map. Adds the drawing tools to the map if none exist.

| Usage | Returns |
|---|---|
| `Map.drawingTools()` | ui.Map.DrawingTools |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.getBounds

Returns the bounds of the current map view, as a list in the format \[west, south, east, north\] in degrees.

| Usage | Returns |
|---|---|
| `Map.getBounds(*asGeoJSON*)` | GeoJSONGeometry\|List\[Number\]\|String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `asGeoJSON` | Boolean, optional | If true, returns map bounds as GeoJSON. |

## ui.Map.getCenter

Returns the coordinates at the center of the map.

| Usage | Returns |
|---|---|
| `Map.getCenter()` | Geometry.Point |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.getScale

Returns the approximate pixel scale of the current map view, in meters.

| Usage | Returns |
|---|---|
| `Map.getScale()` | Number\|String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.getZoom

Returns the current zoom level of the map.

| Usage | Returns |
|---|---|
| `Map.getZoom()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.insert

Inserts a widget into to the panel at the specified index.

Returns this panel.

| Usage | Returns |
|---|---|
| `Map.insert(index, widget)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |
| `index` | Number | The index at which to insert the widget. |
| `widget` | ui.Widget | The widget to insert. |

## ui.Map.layers

Returns the list of layers associated with the map.

| Usage | Returns |
|---|---|
| `Map.layers()` | ui.data.ActiveList\[ui.Map.AbstractLayer\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.onChangeBounds

Registers a callback that's fired when the map bounds change. This is fired during pan, zoom, and when the map's bounds are changed programmatically.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeBounds(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | The callback to fire when the map bounds change. The callback is passed two parameters: an object containing the coordinates of the new map center (with keys lon, lat, and zoom) and the map widget itself. |

## ui.Map.onChangeCenter

Registers a callback that's fired when the map center changes. This is fired during pan or when the map's center is changed programmatically.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeCenter(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | The callback to fire when the map center changes. The callback is passed two parameters: an object containing the coordinates of the new center (with keys lon and lat) and the map widget itself. |

## ui.Map.onChangeZoom

Registers a callback that's fired when the map zoom level changes.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onChangeZoom(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | The callback to fire when the map zoom change. The callback is passed two parameters: the new zoom level and the map widget itself. |

## ui.Map.onClick

Registers a callback that's fired when the map is clicked.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onClick(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | The callback to fire when the map is clicked. The callback is passed an object containing the coordinates of the clicked point on the map (with keys lon and lat) and the map widget itself. |

## ui.Map.onIdle

Registers a callback that's fired when the map stops moving.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onIdle(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | The callback to fire when the map becomes idle. The callback is passed two parameters: an object containing the coordinates of the map center (with keys lon, lat, and zoom) and the map widget itself. |

## ui.Map.onTileLoaded

Registers a callback that's fired when a map tile has been loaded.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Map.onTileLoaded(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `callback` | Function | Called with an array of per layer values. Each value is the fraction of tiles still pending: a value of 0 means there are no more tiles to load for the layer. |

## ui.Map.remove

Removes the given item from the map, if it exists.

Returns the removed item or null if it hadn't been added to the map.

| Usage | Returns |
|---|---|
| `Map.remove(item)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `item` | Object | The item to remove. |

## ui.Map.setCenter

Centers the map view at the given coordinates with the given zoom level. If no zoom level is provided, it uses the most recent zoom level on the map.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setCenter(lon, lat, *zoom*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `lon` | Number | The longitude of the center, in degrees. |
| `lat` | Number | The latitude of the center, in degrees. |
| `zoom` | Number, optional | The zoom level, from 0 to 24. |

## ui.Map.setControlVisibility

Sets the visibility of the controls on the map.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setControlVisibility(*all*, *layerList*, *zoomControl*, *scaleControl*, *mapTypeControl*, *fullscreenControl*, *drawingToolsControl*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `all` | Boolean, optional | Whether to show all controls. False hides all controls; true shows all controls. Overridden by individually set parameters. Note that setting this explicitly will affect any additional controls added in the future. |
| `layerList` | Boolean, optional | When false, hides the layer list panel or, when true, allows the layer list panel's visibility to be determined by the presence of layers in the list. The default is to show the list. |
| `zoomControl` | Boolean, optional | Whether the zoom control is visible. Defaults to true. |
| `scaleControl` | Boolean, optional | Whether to show the control which indicates the scale at the map's current zoom level. Defaults to true. |
| `mapTypeControl` | Boolean, optional | Whether to show the control that allows the user to change the base map. Defaults to true. |
| `fullscreenControl` | Boolean, optional | Whether to show the control that allows the user to make the map full-screen. Defaults to true. |
| `drawingToolsControl` | Boolean, optional | Whether to show the control that allows the user to add or edit the geometry drawing tools. Defaults to true if the drawing tools were previously added to the map. Ignored if the drawing tools were not previously added to the map. |

## ui.Map.setGestureHandling

Controls how gestures are handled on the map.

See https://developers.google.com/maps/documentation/javascript/reference/map#MapOptions.gestureHandling.

| Usage | Returns |
|---|---|
| `Map.setGestureHandling(option)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `option` | String | The option that controls how gestures are handled on the map. Allowed values: - "cooperative": Scroll events and one-finger touch gestures scroll the page, and do not zoom or pan the map. Two-finger touch gestures pan and zoom the map. Scroll events with a ctrl key or ⌘ key pressed zoom the map. In this mode the map cooperates with the page. - "greedy": All touch gestures and scroll events pan or zoom the map. - "none": The map cannot be panned or zoomed by user gestures. - "auto": (default) Gesture handling is either cooperative or greedy, depending on whether the page is scrollable or in an iframe. |

## ui.Map.setLocked

Limits panning and zooming on the map.

- To lock both panning and zooming, set locked to true and nothing else.

- To allow panning and limit the min and max zoom, set locked to false and supply the minZoom and maxZoom parameters.

- To disallow panning and limit min and max zoom, set locked to true and supply the minZoom and maxZoom parameters.

- To reset the map to default, set locked to false and nothing else.

| Usage | Returns |
|---|---|
| `Map.setLocked(locked, *minZoom*, *maxZoom*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `locked` | Boolean | Whether the map should be locked or not. |
| `minZoom` | Number, optional | (optional) The minimum zoom for the map, between 0 and 24, inclusive. |
| `maxZoom` | Number, optional | (optional) The maximum zoom for the map, between 0 and 24, inclusive. |

## ui.Map.setOptions

Modifies the Google Maps basemap. Allows for: 1) Setting the current MapType. 2) Providing custom styles for the basemap (MapTypeStyles). 3) Setting the list of available mapTypesIds for the basemap.

If called with no parameters, resets the map type to the Google Maps default.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setOptions(*mapTypeId*, *styles*, *types*)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `mapTypeId` | String, optional | A mapTypeId to set the basemap to. Can be one of "ROADMAP", "SATELLITE", "HYBRID", or "TERRAIN" to select one of the standard Google Maps API map types, or one of the keys specified in the opt_styles dictionary. If left as null and only 1 style is specified in opt_styles, that style will be used. |
| `styles` | Object, optional | A dictionary of custom MapTypeStyle objects keyed with a name that will appear in the map's Map Type Controls. See: https://developers.google.com/maps/documentation/javascript/reference#MapTypeStyle |
| `types` | List\[String\], optional | A list of mapTypeIds to make available. If omitted, but opt_styles is specified, appends all of the style keys to the standard Google Maps API map types. |

## ui.Map.setZoom

Sets the zoom level of the map.

Returns this ui.Map.

| Usage | Returns |
|---|---|
| `Map.setZoom(zoom)` | ui.Map |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `zoom` | Number | The zoom level, from 0 to 24, to set for the map. |

## ui.Map.style

Returns the map's style ActiveDictionary, which can be modified to update the map's styles.

In addition to the standard UI API styles listed in the ui.Panel.style() documentation, ui.Map supports the following custom style option:

- cursor, which can be 'crosshair' or 'hand' (default)

| Usage | Returns |
|---|---|
| `Map.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |

## ui.Map.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Map.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.map` | ui.Map | The ui.Map instance. |
| `idOrType` | String, optional | Either an ID returned by listen() when a callback was registered, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks registered with that event type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Map.widgets

Returns the list of widgets currently in the panel.

| Usage | Returns |
|---|---|
| `Map.widgets()` | ui.data.ActiveList\[ui.Widget\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |

## ui.Panel

A widget that can hold other widgets. Use panels to construct complex combinations of nested widgets.

Panels can be added to ui.root but not printed to the console with print().

| Usage | Returns |
|---|---|
| `ui.Panel(*widgets*, *layout*, *style*)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| `widgets` | List\[ui.Widget\]\|ui.Widget, optional | The list of widgets or a single widget to add to the panel. Defaults to an empty array. |
| `layout` | String\|ui.Panel.Layout, optional | The layout to use for this panel. If a string is passed in, it's taken as a shortcut to the layout constructor with that name. Defaults to 'flow'. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |

## ui.Panel.Layout.absolute

Returns a layout that places its widgets absolutely relative to the panel.

An added widget's "position" style property determines how it is placed. The following positions are supported:

- top-left, top-center, top-right

- middle-left, middle-right

- bottom-left, bottom-center, bottom-right

If no position is specified, the widget will be placed behind (that is, with a lower z-index than) the positioned widgets.

| Usage | Returns |
|---|---|
| `ui.Panel.Layout.absolute()` | ui.Panel.Layout |

**No arguments.**

## ui.Panel.Layout.flow

Returns a layout that places its widgets in a flow, either horizontal or vertical. By default, widgets take up their natural space within a flow layout panel. Set the "stretch" style property on an added widget to stretch it to fill available space in the relevant direction: - horizontal, vertical, both When multiple widgets are stretched, the available space is split equally among them. Panels are widgets themselves and can be stretched by specifying a "stretch" style property.

| Usage | Returns |
|---|---|
| `ui.Panel.Layout.flow(*direction*, *wrap*)` | ui.Panel.Layout |

| Argument | Type | Details |
|---|---|---|
| `direction` | String, optional | The direction of the flow. One of 'horizontal' or 'vertical'. Defaults to 'vertical'. |
| `wrap` | Boolean, optional | Whether to wrap children in the layout if there are too many to show in one line. Defaults to false. |

## ui.Panel.add

Adds a widget to the panel.

Returns this panel.

| Usage | Returns |
|---|---|
| `Panel.add(widget)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |
| `widget` | ui.Widget | The widget to be added. |

## ui.Panel.clear

Removes all widgets from the panel.

Returns this panel.

| Usage | Returns |
|---|---|
| `Panel.clear()` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |

## ui.Panel.getLayout

Gets the panel's layout.

| Usage | Returns |
|---|---|
| `Panel.getLayout()` | ui.Panel.Layout |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |

## ui.Panel.insert

Inserts a widget into to the panel at the specified index.

Returns this panel.

| Usage | Returns |
|---|---|
| `Panel.insert(index, widget)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |
| `index` | Number | The index at which to insert the widget. |
| `widget` | ui.Widget | The widget to insert. |

## ui.Panel.remove

Removes the given widget from the panel, if it exists.

Returns whether the widget was successfully removed.

| Usage | Returns |
|---|---|
| `Panel.remove(widget)` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |
| `widget` | ui.Widget | The widget to remove. |

## ui.Panel.setLayout

Sets the panel's layout.

Returns this panel.

| Usage | Returns |
|---|---|
| `Panel.setLayout(layout)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |
| `layout` | ui.Panel.Layout | The new layout. |

## ui.Panel.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Panel.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Panel.widgets

Returns the list of widgets currently in the panel.

| Usage | Returns |
|---|---|
| `Panel.widgets()` | ui.data.ActiveList\[ui.Widget\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.panel` | ui.Panel | The ui.Panel instance. |

## ui.Select

A printable select menu with a callback.

| Usage | Returns |
|---|---|
| `ui.Select(*items*, *placeholder*, *value*, *onChange*, *disabled*, *style*)` | ui.Select |

| Argument | Type | Details |
|---|---|---|
| `items` | List\[Object\], optional | The list of options to add to the select. Defaults to an empty array. |
| `placeholder` | String, optional | The placeholder shown when no value is selected. Defaults to "Select a value...". |
| `value` | String, optional | The select's value. Defaults to null. |
| `onChange` | Function, optional | The callback to fire when an item is selected. The callback is passed the currently selected value and the select widget. |
| `disabled` | Boolean, optional | Whether the select is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |

## ui.Select.getDisabled

Returns whether the select is disabled.

| Usage | Returns |
|---|---|
| `Select.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |

## ui.Select.getPlaceholder

Returns the select's placeholder text.

| Usage | Returns |
|---|---|
| `Select.getPlaceholder()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |

## ui.Select.getValue

Returns the currently selected value.

| Usage | Returns |
|---|---|
| `Select.getValue()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |

## ui.Select.items

See ui.data.ActiveList.

Returns the list of items in the selection menu.

| Usage | Returns |
|---|---|
| `Select.items()` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |

## ui.Select.onChange

Registers a callback that's fired when an item is selected.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Select.onChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |
| `callback` | Function | The callback to fire when an item is selected. The callback is passed the currently selected value and the select widget. |

## ui.Select.setDisabled

Sets whether the select is disabled.

Returns this select.

| Usage | Returns |
|---|---|
| `Select.setDisabled(disabled)` | ui.Select |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |
| `disabled` | Boolean | Whether the select is disabled. |

## ui.Select.setPlaceholder

Sets the select's placeholder text, which is shown when no value is selected.

Returns this select.

| Usage | Returns |
|---|---|
| `Select.setPlaceholder(placeholder)` | ui.Select |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |
| `placeholder` | String | The select's placeholder text. |

## ui.Select.setValue

Sets the selected value.

Returns this select.

| Usage | Returns |
|---|---|
| `Select.setValue(value, *trigger*)` | ui.Select |

| Argument | Type | Details |
|---|---|---|
| this: `ui.select` | ui.Select | The ui.Select instance. |
| `value` | String | The value to select. |
| `trigger` | Boolean, optional | Whether to trigger onChange callbacks when the value property changes. Defaults to true. |

## ui.Select.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Select.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Select.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Select.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Slider

A draggable target that ranges linearly between two numeric values. The value of the slider is displayed as a label alongside it.

| Usage | Returns |
|---|---|
| `ui.Slider(*min*, *max*, *value*, *step*, *onChange*, *direction*, *disabled*, *style*)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| `min` | Number, optional | The minimum value. Defaults to 0. |
| `max` | Number, optional | The maximum value. Defaults to 1. |
| `value` | Number, optional | The initial value. Defaults to 0. |
| `step` | Number, optional | The step size for the slider. Defaults to 0.01. |
| `onChange` | Function, optional | A callback to fire when the slider's state changes. The callback is passed the slider's current value and the slider widget. |
| `direction` | String, optional | The direction of the slider. One of 'horizontal' or 'vertical'. Defaults to 'horizontal'. |
| `disabled` | Boolean, optional | Whether the slider is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |

## ui.Slider.getDisabled

Returns whether the slider is disabled.

| Usage | Returns |
|---|---|
| `Slider.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |

## ui.Slider.getMax

Returns the slider's maximum value.

| Usage | Returns |
|---|---|
| `Slider.getMax()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |

## ui.Slider.getMin

Returns the slider's minimum value.

| Usage | Returns |
|---|---|
| `Slider.getMin()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |

## ui.Slider.getStep

Returns the slider's step value.

| Usage | Returns |
|---|---|
| `Slider.getStep()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |

## ui.Slider.getValue

Returns the current slider value.

| Usage | Returns |
|---|---|
| `Slider.getValue()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |

## ui.Slider.onChange

Registers a callback that's fired when the slider's state changes. If the change is due to the user dragging the slider, the event will not fire until the drag completes.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Slider.onChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `callback` | Function | The callback to fire when the slider's state changes. The callback is passed the slider's current value and the slider widget. |

## ui.Slider.onSlide

Registers a callback that's fired when the slider's state changes. The callback will be invoked repeatedly while the user is dragging the slider.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Slider.onSlide(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `callback` | Function | The callback to fire when the slider's state changes. The callback is passed the slider's current value. |

## ui.Slider.setDisabled

Sets whether the slider is disabled.

Returns this slider.

| Usage | Returns |
|---|---|
| `Slider.setDisabled(disabled)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `disabled` | Boolean | Whether the slider is disabled. |

## ui.Slider.setMax

Sets the maximum value of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `Slider.setMax(value)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `value` | Number | The slider's maximum value. |

## ui.Slider.setMin

Sets the minimum value of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `Slider.setMin(value)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `value` | Number | The slider's minimum value. |

## ui.Slider.setStep

Sets the step value of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `Slider.setStep(value)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `value` | Number | The slider's step value. |

## ui.Slider.setValue

Set the value of the slider.

Returns this slider.

| Usage | Returns |
|---|---|
| `Slider.setValue(value, *trigger*)` | ui.Slider |

| Argument | Type | Details |
|---|---|---|
| this: `ui.slider` | ui.Slider | The ui.Slider instance. |
| `value` | Number | The value to slider. |
| `trigger` | Boolean, optional | Whether to trigger onChange callbacks when the value property changes. Defaults to true. |

## ui.Slider.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Slider.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Slider.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Slider.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.SplitPanel

A widget containing two panels with a divider between them. The divider can be dragged, allowing the panels to be resized. One or both panels may be ui.Map objects.

By default the layout initializes with a 50/50 split. The width and max/minWidth styles on the panels control the split sizing for horizontal orientations. Similarly, use height and max/minHeight for vertical. These can be given in pixels as '{n}px' or as a percentage of the containing SplitPanel as '{n}%'.

Note that the given size for the second panel will be ignored if the first panel size is specified, since the overall width of the split panel is controlled independently. Max/min sizes may be set for both panels.

| Usage | Returns |
|---|---|
| `ui.SplitPanel(*firstPanel*, *secondPanel*, *orientation*, *wipe*, *style*)` | ui.SplitPanel |

| Argument | Type | Details |
|---|---|---|
| `firstPanel` | ui.Panel, optional | The left or top panel. Defaults to a new instance of ui.Panel. |
| `secondPanel` | ui.Panel, optional | The bottom or right panel. Defaults to a new instance of ui.Panel. |
| `orientation` | String, optional | One of "horizontal" or "vertical". Defaults to "horizontal". |
| `wipe` | Boolean, optional | Whether to enable the wiping effect. When this mode is enabled, both panels take up all available space, and dragging the divider doesn't set the size of the panels but rather determines how much of each panel is shown. This effect is analogous to a "wipe transition". This mode is useful for comparing two maps. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this panel. Defaults to an empty object. |

## ui.SplitPanel.getFirstPanel

Returns the first panel in the split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.getFirstPanel()` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |

## ui.SplitPanel.getOrientation

Returns the panel's orientation.

| Usage | Returns |
|---|---|
| `SplitPanel.getOrientation()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |

## ui.SplitPanel.getPanel

Returns the requested panel in the split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.getPanel(index)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `index` | Number | 0 for top or left panel, 1 for bottom or right panel. |

## ui.SplitPanel.getSecondPanel

Returns the second panel in the split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.getSecondPanel()` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |

## ui.SplitPanel.getWipe

Returns whether the wiping effect is enabled.

| Usage | Returns |
|---|---|
| `SplitPanel.getWipe()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |

## ui.SplitPanel.setFirstPanel

Returns this split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.setFirstPanel(panel)` | ui.SplitPanel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `panel` | ui.Panel | The panel to display left or on top of the split. |

## ui.SplitPanel.setOrientation

Sets the panel's orientation; one of "horizontal" or "vertical".

Returns this split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.setOrientation(orientation)` | ui.SplitPanel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `orientation` | String | The new orientation. |

## ui.SplitPanel.setPanel

Returns the requested panel in the split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.setPanel(index, panel)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `index` | Number | 0 for top or left panel, 1 for bottom or right panel. |
| `panel` | ui.Panel | The panel to add to the split panel. |

## ui.SplitPanel.setSecondPanel

Returns this split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.setSecondPanel(panel)` | ui.SplitPanel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `panel` | ui.Panel | The panel to display right of or below the split. |

## ui.SplitPanel.setWipe

Enables or disables the wiping effect.

Returns this split panel.

| Usage | Returns |
|---|---|
| `SplitPanel.setWipe(wipe)` | ui.SplitPanel |

| Argument | Type | Details |
|---|---|---|
| this: `ui.splitpanel` | ui.SplitPanel | The ui.SplitPanel instance. |
| `wipe` | Boolean | Whether to enable the wiping effect. |

## ui.SplitPanel.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `SplitPanel.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.SplitPanel.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `SplitPanel.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Textbox

A textbox that enables the user to input text information.

| Usage | Returns |
|---|---|
| `ui.Textbox(*placeholder*, *value*, *onChange*, *disabled*, *style*)` | ui.Textbox |

| Argument | Type | Details |
|---|---|---|
| `placeholder` | String, optional | The placeholder text to display when the textbox is empty. Defaults to none. |
| `value` | String, optional | The textbox's value. Defaults to none. |
| `onChange` | Function, optional | The callback to fire when the text changes. The callback is passed the text currently in the textbox and the textbox widget. |
| `disabled` | Boolean, optional | Whether the textbox is disabled. Defaults to false. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this widget. See style() documentation. |

## ui.Textbox.getDisabled

Returns whether the textbox is disabled.

| Usage | Returns |
|---|---|
| `Textbox.getDisabled()` | Boolean |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |

## ui.Textbox.getPlaceholder

Returns the textbox's placeholder text.

| Usage | Returns |
|---|---|
| `Textbox.getPlaceholder()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |

## ui.Textbox.getValue

Returns the value of the textbox.

| Usage | Returns |
|---|---|
| `Textbox.getValue()` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |

## ui.Textbox.onChange

Registers a callback that's called when text in the textbox changes.

In particular, the callback is called when:

- The user types a new value and then either the textbox loses focus or the user presses enter.

- A new value is set programmatically with set('value', newValue).

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Textbox.onChange(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |
| `callback` | Function | The callback to fire when the text changes. The callback is passed the text currently in the textbox and the textbox widget. |

## ui.Textbox.setDisabled

Sets whether the textbox is disabled.

Returns this textbox.

| Usage | Returns |
|---|---|
| `Textbox.setDisabled(disabled)` | ui.Textbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |
| `disabled` | Boolean | Whether the textbox is disabled. |

## ui.Textbox.setPlaceholder

Sets the textbox's placeholder text, which is shown when no text is entered.

Returns this select.

| Usage | Returns |
|---|---|
| `Textbox.setPlaceholder(placeholder)` | ui.Textbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |
| `placeholder` | String | The select's placeholder text. |

## ui.Textbox.setValue

Sets the value of the textbox.

Returns this textbox.

| Usage | Returns |
|---|---|
| `Textbox.setValue(value, *trigger*)` | ui.Textbox |

| Argument | Type | Details |
|---|---|---|
| this: `ui.textbox` | ui.Textbox | The ui.Textbox instance. |
| `value` | String | The value of the textbox. |
| `trigger` | Boolean, optional | Whether to trigger onChange callbacks when the value property changes. Defaults to true. |

## ui.Textbox.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Textbox.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Textbox.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Textbox.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.Thumbnail

A fixed-size thumbnail image generated asynchronously from an ee.Image.

| Usage | Returns |
|---|---|
| `ui.Thumbnail(*image*, *params*, *onClick*, *style*)` | ui.Thumbnail |

| Argument | Type | Details |
|---|---|---|
| `image` | Image, optional | The ee.Image from which to generate the thumbnail. Defaults to an empty ee.Image. |
| `params` | Object, optional | For an explanation of the possible parameters, see ui.Thumbnail.setParams(). Defaults to an empty object. |
| `onClick` | Function, optional | A callback fired when the thumbnail is clicked. |
| `style` | Object, optional | An object of allowed CSS styles with their values to be set for this label. Defaults to an empty object. |

## ui.Thumbnail.getImage

Returns the ee.Image for the thumbnail.

| Usage | Returns |
|---|---|
| `Thumbnail.getImage()` | Image\|ImageCollection |

| Argument | Type | Details |
|---|---|---|
| this: `ui.thumbnail` | ui.Thumbnail | The ui.Thumbnail instance. |

## ui.Thumbnail.getParams

See ee.Image.prototype.getThumbnailURL.

Returns the parameters used in generating the thumbnail.

| Usage | Returns |
|---|---|
| `Thumbnail.getParams()` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.thumbnail` | ui.Thumbnail | The ui.Thumbnail instance. |

## ui.Thumbnail.onClick

Registers a callback that's fired when the thumbnail is clicked.

Returns an ID which can be passed to unlisten() to unregister the callback.

| Usage | Returns |
|---|---|
| `Thumbnail.onClick(callback)` | String |

| Argument | Type | Details |
|---|---|---|
| this: `ui.thumbnail` | ui.Thumbnail | The ui.Thumbnail instance. |
| `callback` | Function | The callback to fire when the thumbnail is clicked. The callback is passed the thumbnail widget. |

## ui.Thumbnail.setImage

Sets the ee.Image used to generate the thumbnail.

Returns this thumbnail.

| Usage | Returns |
|---|---|
| `Thumbnail.setImage(image)` | ui.Thumbnail |

| Argument | Type | Details |
|---|---|---|
| this: `ui.thumbnail` | ui.Thumbnail | The ui.Thumbnail instance. |
| `image` | Image | The image from which to generate the thumbnail. |

## ui.Thumbnail.setParams

Sets the parameters used to generate the thumbnail.

Returns this thumbnail.

| Usage | Returns |
|---|---|
| `Thumbnail.setParams(params)` | ui.Thumbnail |

| Argument | Type | Details |
|---|---|---|
| this: `ui.thumbnail` | ui.Thumbnail | The ui.Thumbnail instance. |
| `params` | Object | The parameters used in generating the thumbnail. |---| | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling. | | ` region ` (E,S,W,N or GeoJSON) Geospatial region of the image to render. By default, the whole image. | | ` format ` (string) Either 'png' or 'jpg'. | | ` bands ` (comma-separated strings) Comma-delimited list of band names to be mapped to RGB. | | ` min ` (comma-separated numbers) Value (or one per band) to map onto 00. | | ` max ` (comma-separated numbers) Value (or one per band) to map onto FF. | | ` gain ` (comma-separated numbers) Gain (or one per band) to map onto 00-FF. | | ` bias ` (comma-separated numbers) Offset (or one per band) to map onto 00-FF. | | ` gamma ` (comma-separated numbers) Gamma correction factor (or one per band) | | ` palette ` (comma-separated strings) List of CSS-style color strings (single-band previews only). | | ` opacity ` (number) a number between 0 and 1 for opacity. | | ` version ` (number) Version number of image (or latest). | |

## ui.Thumbnail.style

Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles.

Properties which behave like their CSS counterparts:

- height, maxHeight, minHeight (e.g. '100px')

- width, maxWidth, minWidth (e.g. '100px')

- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')

- color, backgroundColor (e.g. 'red' or '#FF0000')

- border (e.g. '1px solid black')

- borderColor (e.g. 'red black blue #FF0000')

- borderRadius (e.g. '10px')

- borderStyle (e.g. 'solid dashed none dotted')

- borderWidth (e.g. '1px 0px 1px 0px')

- fontSize (e.g. '24px')

- fontStyle (e.g. 'italic')

- fontWeight (e.g. 'bold' or '100')

- fontFamily (e.g. 'monospace' or 'serif')

- textAlign (e.g. 'left' or 'center')

- textDecoration (e.g. 'underline' or 'line-through')

- whiteSpace (e.g. 'nowrap' or 'pre')

- shown (true or false)

Supported custom layout properties (see ui.Panel.Layout documentation):

- stretch ('horizontal', 'vertical', 'both')

- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)

| Usage | Returns |
|---|---|
| `Thumbnail.style()` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |

## ui.Thumbnail.unlisten

Deletes callbacks.

| Usage | Returns |
|---|---|
| `Thumbnail.unlisten(*idOrType*)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.widget` | ui.Widget | The ui.Widget instance. |
| `idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted. |

## ui.data.ActiveDictionary

A dictionary-like container for data for use in UI components.

When a property of a ui.data.ActiveDictionary (e.g. myButton.style()) is updated, the component it belongs to is automatically updated. For example, myButton.style().set('color', 'red') would change the color of button's text to red.

| Usage | Returns |
|---|---|
| `ui.data.ActiveDictionary(*object*, *allowedProperties*)` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| `object` | Object, optional | A JavaScript object with properties and values to initialize this object with. |
| `allowedProperties` | List\[String\], optional | An array of allowed properties for this object. If undefined, then any property is allowed. |

## ui.data.ActiveDictionary.get

Returns either a clone of this object or, if a key is provided, the value of the property with the passed-in key. Look at the constructor's parameters to see which properties are available.

| Usage | Returns |
|---|---|
| `ActiveDictionary.get(*key*)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `key` | String, optional | The key of the property to retrieve. |

## ui.data.ActiveDictionary.set

Sets the value of a given property. Throws an error if the key provided is not supported by the object. Look at the constructor's parameters to see which properties can be set.

Returns this ui.data.ActiveDictionary.

| Usage | Returns |
|---|---|
| `ActiveDictionary.set(keyOrDict, *value*)` | ui.data.ActiveDictionary |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activedictionary` | ui.data.ActiveDictionary | The ui.data.ActiveDictionary instance. |
| `keyOrDict` | Object\|String | Either the key of the property to set or a dictionary of key/value pairs to set on the object. |
| `value` | Object, optional | The property's new value. This is required when the first argument is a key string. |

## ui.data.ActiveList

An array-like container for data for use in UI components.

When a ui.data.ActiveList (e.g. Map.layers()) is updated, the component it belongs to is updated as well. For example, Map.layers().add(myLayer) will add myLayer as a layer on the map.

| Usage | Returns |
|---|---|
| `ui.data.ActiveList(*list*)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| `list` | List\[Object\], optional | An optional list to initialize with. |

## ui.data.ActiveList.add

Appends an element to the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `ActiveList.add(el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `el` | Object | The element to add. |

## ui.data.ActiveList.forEach

Iterates over each element, calling the provided callback. The callback is called for each element like: callback(element, index).

| Usage | Returns |
|---|---|
| `ActiveList.forEach(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `callback` | Function |   |

## ui.data.ActiveList.get

Returns the element at the specified index.

| Usage | Returns |
|---|---|
| `ActiveList.get(index)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index of the element to return. |

## ui.data.ActiveList.getJsArray

Returns the list as a JS array.

| Usage | Returns |
|---|---|
| `ActiveList.getJsArray()` | List\[Object\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |

## ui.data.ActiveList.insert

Inserts an element at the specified index and shifts the rest of the list. If the specified index is greater than the length of the list, the element will be appended to the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `ActiveList.insert(index, el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index at which to insert the element. |
| `el` | Object | The element to insert. |

## ui.data.ActiveList.length

Returns the number of elements in the list.

| Usage | Returns |
|---|---|
| `ActiveList.length()` | Number |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |

## ui.data.ActiveList.remove

Removes the specified element from the list.

Returns the removed element or null if the element was not present in the list.

| Usage | Returns |
|---|---|
| `ActiveList.remove(el)` | Object |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `el` | Object | The element to remove. |

## ui.data.ActiveList.reset

Replaces all elements in list with a new list or, if no list is provided, removes all elements from list.

Returns the elements in the list after the reset is applied.

| Usage | Returns |
|---|---|
| `ActiveList.reset(*list*)` | List\[Object\] |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `list` | List\[Object\], optional | A list of elements. |

## ui.data.ActiveList.set

Sets an element at the specified index. If the index exceeds that of the list's last element, the element will be added to the end of the list.

Returns this ui.data.ActiveList.

| Usage | Returns |
|---|---|
| `ActiveList.set(index, el)` | ui.data.ActiveList |

| Argument | Type | Details |
|---|---|---|
| this: `ui.data.activelist` | ui.data.ActiveList | The ui.data.ActiveList instance. |
| `index` | Number | The index to overwrite. |
| `el` | Object | The element to set. |

## ui.root.add

Adds a widget to the root panel.

Returns the root panel.

| Usage | Returns |
|---|---|
| `ui.root.add(widget)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| `widget` | ui.Widget | The widget to be added. |

## ui.root.clear

Clears the root panel.

| Usage | Returns |
|---|---|
| `ui.root.clear()` |   |

**No arguments.**

## ui.root.getLayout

Returns the root panel's layout.

| Usage | Returns |
|---|---|
| `ui.root.getLayout()` | ui.Panel.Layout |

**No arguments.**

## ui.root.insert

Inserts a widget into to the root panel at the specified index. Returns the root panel.

| Usage | Returns |
|---|---|
| `ui.root.insert(index, widget)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| `index` | Number | The index at which to insert the widget. |
| `widget` | ui.Widget | The widget to insert. |

## ui.root.onResize

Registers a callback that's fired when the script starts and whenever the browser window size changes. It will be passed an object with boolean fields "is_mobile", "is_tablet", "is_desktop", "is_portrait" and "is_landscape", and numeric fields "width" and "height".

These fields indicate whether a user's device is mobile, tablet or desktop, the device orientation (portrait or landscape), and the width and height of the window in pixels. See the Width and Height (dp) section of device metrics at https://material.io/resources/devices/.

| Usage | Returns |
|---|---|
| `ui.root.onResize(callback)` |   |

| Argument | Type | Details |
|---|---|---|
| `callback` | Function | The callback to fire after the window has been resized. The callback is passed an object with the information of the device. |

## ui.root.remove

Removes the given widget from the root panel, if it exists.

Returns the removed widget or null if the widget was not present in the root panel.

| Usage | Returns |
|---|---|
| `ui.root.remove(widget)` | Object |

| Argument | Type | Details |
|---|---|---|
| `widget` | ui.Widget | The widget to remove. |

## ui.root.setKeyHandler

Sets a keydown event handler to the root panel with a non-predefined key. The handler is fired only once when a user presses the bound key command. The same key will be bound to the latest handler set to it.

| Usage | Returns |
|---|---|
| `ui.root.setKeyHandler(keyCode, handler, *description*)` |   |

| Argument | Type | Details |
|---|---|---|
| `keyCode` | List\[ui.Key\]\|ui.Key | A key code or an array of key codes. For example, ui.Key.A or \[ui.Key.SHIFT, ui.Key.A\]. |
| `handler` | Function | The handler for the key command. |
| `description` | String, optional | A short description that explains this key command. The description will be visible in the Shortcuts Menu. |

## ui.root.setLayout

Sets the ui.root panel's layout.

Returns the root panel.

| Usage | Returns |
|---|---|
| `ui.root.setLayout(layout)` | ui.Panel |

| Argument | Type | Details |
|---|---|---|
| `layout` | String\|ui.Panel.Layout | The root panel's new layout. |

## ui.root.widgets

Returns the list of widgets currently in the root panel.

| Usage | Returns |
|---|---|
| `ui.root.widgets()` | ui.data.ActiveList |

**No arguments.**

## ui.url.get

Returns the value of the given key from the URL fragment.

| Usage | Returns |
|---|---|
| `ui.url.get(key, *default*)` | Boolean\|Number\|Object\|String |

| Argument | Type | Details |
|---|---|---|
| `key` | String | The name of the parameter to read. |
| `default` | Boolean\|Number\|String, optional | optional default value to return if no value is present. |

## ui.url.set

Sets the value of the page's URL fragment. The fragment encodes a dictionary of keys and values. If a dictionary is supplied as the first argument, the key/value pairs in that dictionary will be encoded and replace the current URL fragment. If a key string is provided, then only that key (and its value, the second argument) are updated, and the rest of the URL fragment is unchanged.

| Usage | Returns |
|---|---|
| `ui.url.set(keyOrDict, *value*)` |   |

| Argument | Type | Details |
|---|---|---|
| `keyOrDict` | Dictionary\[Object\]\|String | Either a key to update a single value in the URL fragment, or a dictionary of key/value pairs which will replace the existing URL fragment. Dictionary values must be of type string, number, or boolean. |
| `value` | Boolean\|Number\|String, optional | The new value to associate with a single key. This is required when the first argument is a string and is otherwise ignored. |

## ui.util.clear

Clears all state related to utility functions, including cancelling any active timeouts, intervals, debounces, etc.

| Usage | Returns |
|---|---|
| `ui.util.clear()` |   |

**No arguments.**

## ui.util.clearTimeout

Clears a timeout set via ui.util.setTimeout or ui.util.setInterval.

| Usage | Returns |
|---|---|
| `ui.util.clearTimeout(timeoutKey)` |   |

| Argument | Type | Details |
|---|---|---|
| `timeoutKey` | Number | The key to the timeout or interval to clear. |

## ui.util.debounce

Wraps a function to allow it to be called, at most, once for each sequence of calls fired repeatedly so long as they are fired less than a specified interval apart (in milliseconds). This can be used to reduce the number of invocations of an expensive function while ensuring it eventually runs.

Example use: For the callback to a change event on a ui.Checkbox. If the user clicks the checkbox repeatedly, only the last click of the checkbox will run the callback.

Returns the debounced function.

| Usage | Returns |
|---|---|
| `ui.util.debounce(func, delay, *scope*)` | Function |

| Argument | Type | Details |
|---|---|---|
| `func` | Function | The function to debounce. |
| `delay` | Number | After the function is called once, the number of milliseconds to delay for an additional invocation of the function before allowing it to run. |
| `scope` | Object, optional | Object in whose scope to call the function. |

## ui.util.getCurrentPosition

Gets the user's current geographic position from the browser's geolocation service.

| Usage | Returns |
|---|---|
| `ui.util.getCurrentPosition(success, *error*)` |   |

| Argument | Type | Details |
|---|---|---|
| `success` | Function | A callback function that takes a ee.Geometry.Point object as its input parameter. |
| `error` | Function, optional | An optional callback function that takes an error message as its input parameter. |

## ui.util.rateLimit

Wraps a function to allow it to be called, at most, once per interval. If the wrapper function is called more than once, only the first call will go through, and no subsequent invocations will have an effect until the interval has elapsed. This can be used to ensure a function that is expensive to run executes immediately but doesn't execute repeatedly.

Example use: For the callback to a click on a ui.Button, in order to prevent the button from being accidentally double-clicked and the callback running twice.

Returns the rate-limited function.

| Usage | Returns |
|---|---|
| `ui.util.rateLimit(func, delay, *scope*)` | Function |

| Argument | Type | Details |
|---|---|---|
| `func` | Function | Function to call. |
| `delay` | Number | After the function is called and executed, the number of milliseconds to delay before allowing an additional invocation of the function. |
| `scope` | Object, optional | Object in whose scope to call the function. |

## ui.util.setInterval

Repeatedly calls a function with a fixed time delay between each call.

Returns a key that can be passed to ui.util.clearTimeout to remove the timeout.

| Usage | Returns |
|---|---|
| `ui.util.setInterval(func, delay)` | Number |

| Argument | Type | Details |
|---|---|---|
| `func` | Function | The function to run after the specified delay. |
| `delay` | Number | The time, in milliseconds (thousandths of a second), the timer should delay in between executions of the specified function. |

## ui.util.setTimeout

Calls a function after a fixed time delay.

Returns a key that can be passed to ui.util.clearTimeout to remove the timeout.

| Usage | Returns |
|---|---|
| `ui.util.setTimeout(func, delay)` | Number |

| Argument | Type | Details |
|---|---|---|
| `func` | Function | The function to run at the specified interval. |
| `delay` | Number | The time, in milliseconds (thousandths of a second), the timer should delay before execution of the specified function. |

## ui.util.throttle

Wraps a function to allow it to be called, at most, twice per interval. If the wrapper function is called multiple times before the delay elapses, only the first and the last calls will go through.

Example use: For the callback to a slide event on a ui.Slider. The callback will run immediately, making the slide action feel responsive. The callback is also guaranteed to run after the user has finished interacting with the slider, ensuring that the final callback invocation has access to the slider's final value.

Returns the wrapped function.

| Usage | Returns |
|---|---|
| `ui.util.throttle(func, delay, *scope*)` | Function |

| Argument | Type | Details |
|---|---|---|
| `func` | Function | The function to call. |
| `delay` | Number | The delay, in milliseconds, for the throttle. The function can only be called once after the initial invocation until after the delay has elapsed. |
| `scope` | Object, optional | The object in whose scope to call the function. |

