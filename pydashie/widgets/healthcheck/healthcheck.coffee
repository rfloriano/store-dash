class Dashing.Healthcheck extends Dashing.Widget
  ready: ->
    if @get('unordered')
      $(@node).find('ol').remove()
    else
      $(@node).find('ul').remove()

  onData: (data) ->
    if data.failed
      $(@node).addClass('widget-healthcheck-error')
    else
      $(@node).removeClass('widget-healthcheck-error')
