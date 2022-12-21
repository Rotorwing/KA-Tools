/**
 * @param {import("babylonjs")}
 */

function readBitmap(filename){
    filename = filename.replaceAll("-", "_").split(".")[0];
    file = window[filename]
    data = window[filename+"_data"]
    if(data == null || file == null) throw Error("file var or image data was not found!")
    
    width = data[0];
    height = data[1];
    hasAlpha = data[2] == 4;

    let imageData = new Uint8Array(width*height*data[2]);
    for(let i = 0; i < imgaeData.length; i++){
        fileIndex = i*2;
        imageData[i] = parseInt(file[fileIndex]+file[fileIndex+1], 16)
    }

    return new BABYLON.RawTexture.CreateRGBTexture(imageData, width, height, scene);
}