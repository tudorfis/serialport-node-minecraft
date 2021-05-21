
  
const robot = require( 'robotjs' )
const SerialPort = require( 'serialport' )
const Readline = require( '@serialport/parser-readline' )

const port = new SerialPort( 'COM9', { baudRate: 9600 } )
const parser = port.pipe( new Readline({ delimiter: '\n' }))

const mouseSensitivityX = 5
const mouseSensitivityY = 5

let previousMpuX, previousMpuY

parser.on('data', mouseCoordinates => {
   
  const splittedData = mouseCoordinates.split(' ')
  
  const mpuX = +splittedData[ 1 ].replace('y=', '' ) 
  const mpuY = +splittedData[ 2  ].replace('z=', '' ).replace('\r', '') 
  const mpuZ = +splittedData[ 0 ].replace('x=', '' ) 
  
  let mouseX = robot.getMousePos().x,
      mouseY = robot.getMousePos().y

  if ( mpuX > previousMpuX ) {
    mouseX -= mouseSensitivityX
  }
  else if ( mpuX < previousMpuX ) {
    mouseX += mouseSensitivityX
  }

  if ( mpuY > previousMpuY ) {
    mouseY -= mouseSensitivityY
  }
  else if ( mpuY < previousMpuY ) {
    mouseY += mouseSensitivityY
  }

  previousMpuX = mpuX
  previousMpuY = mpuY
  

  robot.moveMouse( mouseX, mouseY )
 // robot.mouseClick()

  console.log({ 
    mouseX, 
    mouseY,
    mpuX,
    mpuY,
    mpuZ 
  })

})