import React from 'react'
import {
  Button,
  Center,
  Image,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Text,
} from '@chakra-ui/react'

const HappyBirthday = () => {

  const { isOpen, onOpen, onClose } = useDisclosure()

  return (
    <div>
      
      <div onClick={onOpen} className='center'>
        <div className='heart'>
        </div>  
      </div>
      {/* <div onClick={onOpen}>Happy Birthday</div> */}

      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Happy Birthday Mama!</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Text align='justify' >Welcome to the beginnings of our website. We can't wait to have even more adventures and document them on here with you</Text>
            <Center>
              <Image
                boxSize='300px'
                src='../LeoKosCrop.png'
                margin='10px'
              />
            </Center>
          </ModalBody>
          <ModalFooter>
            <Button onClick={onClose}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </div>
  )
}

export default HappyBirthday